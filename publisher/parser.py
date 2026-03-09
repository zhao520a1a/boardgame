"""内容解析器 - 读取项目输出，归一化为统一数据结构"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from pathlib import Path

from publisher.config import (
    COPY_FILENAMES,
    COVER_PATTERNS_CN,
    INNER_PATTERNS_CN,
    OUTPUT_DIR_NAMES,
    PROJECT_ROOT,
    RULE_GRAPHIC_PATTERNS,
    STAGE_DIRS,
    STRATEGY_FILENAMES,
    VERSION_DIR_PATTERN,
)
from publisher.models import ImageAsset, NoteContent, TitleCandidate


class ProjectParser:
    """项目内容解析器 - 支持情书(中文)和UNO(英文)两种输出格式"""

    def __init__(self, project_root: str):
        self.project_root = os.path.abspath(project_root)
        if not os.path.isdir(self.project_root):
            raise FileNotFoundError(f"项目目录不存在: {self.project_root}")
        self.game_name = os.path.basename(self.project_root)

    def detect_format(self) -> str:
        """探测项目输出格式: output_cn / output_en / versioned"""
        for name in OUTPUT_DIR_NAMES:
            d = os.path.join(self.project_root, name)
            if os.path.isdir(d):
                # 判断是中文命名还是英文命名
                files = os.listdir(d)
                has_cn = any("封面" in f or "内页" in f for f in files)
                return "output_cn" if has_cn else "output_en"

        if self._find_latest_version():
            return "versioned"

        raise FileNotFoundError(
            f"无法识别项目结构: {self.project_root}\n"
            "请确保存在 '输出/' 或 'output/' 目录，或版本文件夹 v*_*/"
        )

    def parse(self) -> NoteContent:
        """解析项目，返回归一化的 NoteContent"""
        fmt = self.detect_format()
        if fmt == "output_cn":
            output_dir = self._find_output_dir()
            return self._parse_output_cn(output_dir)
        elif fmt == "output_en":
            output_dir = self._find_output_dir()
            return self._parse_output_en(output_dir)
        else:
            version_dir = self._find_latest_version()
            return self._parse_versioned(version_dir)

    # ─── 输出目录查找 ───

    def _find_output_dir(self) -> str:
        for name in OUTPUT_DIR_NAMES:
            d = os.path.join(self.project_root, name)
            if os.path.isdir(d):
                return d
        raise FileNotFoundError("未找到输出目录")

    def _find_latest_version(self) -> str | None:
        """查找最新的版本文件夹"""
        versions = []
        for item in os.listdir(self.project_root):
            if re.match(VERSION_DIR_PATTERN, item):
                versions.append(item)
        if not versions:
            return None
        # 按版本号排序（v2 > v1），同版本号按日期排序
        versions.sort(key=lambda v: (
            int(re.match(VERSION_DIR_PATTERN, v).group(1)),
            re.match(VERSION_DIR_PATTERN, v).group(2),
        ), reverse=True)
        return os.path.join(self.project_root, versions[0])

    # ─── 情书格式解析（中文命名输出目录）───

    def _parse_output_cn(self, output_dir: str) -> NoteContent:
        images = self._scan_images_cn(output_dir)
        copy_path = self._find_file(output_dir, COPY_FILENAMES)
        strategy_path = self._find_file(output_dir, STRATEGY_FILENAMES)

        title_candidates, body, hashtags, full_text = [], "", "", ""
        title = ""
        if copy_path:
            title_candidates, body, hashtags, full_text = self._parse_copy_auto(copy_path)
            selected = [t for t in title_candidates if t.is_selected]
            title = selected[0].text if selected else (
                title_candidates[0].text if title_candidates else ""
            )

        pinned_comment = ""
        scheduled_time = None
        if strategy_path:
            pinned_comment, scheduled_time = self._parse_strategy(strategy_path)

        return NoteContent(
            game_name=self.game_name,
            title=title,
            title_candidates=title_candidates,
            body=body,
            hashtags=hashtags,
            full_text=full_text,
            images=images,
            pinned_comment=pinned_comment,
            scheduled_time=scheduled_time,
        )

    def _scan_images_cn(self, output_dir: str) -> list[ImageAsset]:
        """扫描中文命名的图片文件（同角色去重，优先内页/封面标准命名）"""
        images = []
        png_files = [f for f in os.listdir(output_dir) if f.lower().endswith(".png")]

        for fname in png_files:
            fpath = os.path.join(output_dir, fname)
            role, label, order = self._classify_image_cn(fname)
            if role:
                images.append(ImageAsset(path=fpath, role=role, label=label, order=order))

        # 同角色去重：优先保留"内页"/"封面"标准命名，去掉"文案_P*"等变体
        seen_roles: dict[str, ImageAsset] = {}
        for img in images:
            if img.role not in seen_roles:
                seen_roles[img.role] = img
            else:
                existing = seen_roles[img.role]
                # 优先保留包含"内页"或"封面"的标准命名
                if ("内页" in img.label or "封面" in img.label) and "内页" not in existing.label and "封面" not in existing.label:
                    seen_roles[img.role] = img

        return sorted(seen_roles.values(), key=lambda x: x.order)

    def _classify_image_cn(self, filename: str) -> tuple[str | None, str, int]:
        """根据中文文件名分类图片角色"""
        name = filename.replace(".png", "").replace(".PNG", "")

        # 封面
        for role, patterns in COVER_PATTERNS_CN.items():
            for p in patterns:
                if p in name:
                    return role, name, 1

        # 内页
        for role, patterns in INNER_PATTERNS_CN.items():
            for p in patterns:
                if p in name:
                    order = int(role.split("_p")[1])
                    return role, name, order

        # 规则图
        for p in RULE_GRAPHIC_PATTERNS:
            if p in name.lower():
                # 优先使用极简版
                return "rule_graphic", name, 6

        return None, name, 99

    # ─── UNO格式解析（英文命名输出目录）───

    def _parse_output_en(self, output_dir: str) -> NoteContent:
        images = self._scan_images_en(output_dir)

        # 文案和策略：先在输出目录找，找不到回退到版本文件夹
        copy_path = self._find_file(output_dir, COPY_FILENAMES)
        strategy_path = self._find_file(output_dir, STRATEGY_FILENAMES)

        if not copy_path or not strategy_path:
            version_dir = self._find_latest_version()
            if version_dir:
                if not copy_path:
                    copy_dir = os.path.join(version_dir, STAGE_DIRS["copy"])
                    copy_path = self._find_file(copy_dir, COPY_FILENAMES)
                if not strategy_path:
                    strat_dir = os.path.join(version_dir, STAGE_DIRS["strategy"])
                    strategy_path = self._find_file(strat_dir, STRATEGY_FILENAMES)

        title_candidates, body, hashtags, full_text = [], "", "", ""
        title = ""
        if copy_path:
            title_candidates, body, hashtags, full_text = self._parse_copy_auto(copy_path)
            selected = [t for t in title_candidates if t.is_selected]
            title = selected[0].text if selected else (
                title_candidates[0].text if title_candidates else ""
            )

        pinned_comment = ""
        scheduled_time = None
        if strategy_path:
            pinned_comment, scheduled_time = self._parse_strategy(strategy_path)

        return NoteContent(
            game_name=self.game_name,
            title=title,
            title_candidates=title_candidates,
            body=body,
            hashtags=hashtags,
            full_text=full_text,
            images=images,
            pinned_comment=pinned_comment,
            scheduled_time=scheduled_time,
        )

    def _scan_images_en(self, output_dir: str) -> list[ImageAsset]:
        """扫描英文命名的图片文件（UNO_P1.png 风格）"""
        images = []
        png_files = [f for f in os.listdir(output_dir) if f.lower().endswith(".png")]

        for fname in png_files:
            fpath = os.path.join(output_dir, fname)
            # 匹配 XXX_P1.png ~ XXX_P5.png 格式
            m = re.match(r".*_P(\d+)\.png$", fname, re.IGNORECASE)
            if m:
                page_num = int(m.group(1))
                if page_num == 1:
                    # P1 是封面（默认 B 线高点击率）
                    images.append(ImageAsset(
                        path=fpath, role="cover_b",
                        label=f"{self.game_name}_封面", order=1
                    ))
                elif 2 <= page_num <= 5:
                    role = f"inner_p{page_num}"
                    page_labels = {2: "教学页", 3: "解析页", 4: "场景页", 5: "技巧页"}
                    images.append(ImageAsset(
                        path=fpath, role=role,
                        label=page_labels.get(page_num, f"P{page_num}"),
                        order=page_num,
                    ))

        return sorted(images, key=lambda x: x.order)

    # ─── 版本工作流格式解析 ───

    def _parse_versioned(self, version_dir: str) -> NoteContent:
        images = []

        # 封面
        cover_dir = os.path.join(version_dir, STAGE_DIRS["cover"])
        if os.path.isdir(cover_dir):
            images.extend(self._scan_images_cn(cover_dir))

        # 内页
        inner_dir = os.path.join(version_dir, STAGE_DIRS["inner"])
        if os.path.isdir(inner_dir):
            for img in self._scan_images_cn(inner_dir):
                if img not in images:
                    images.append(img)

        # 规则图
        rule_dir = os.path.join(version_dir, STAGE_DIRS["rule"])
        if os.path.isdir(rule_dir):
            for img in self._scan_images_cn(rule_dir):
                if img.role == "rule_graphic":
                    images.append(img)

        images.sort(key=lambda x: x.order)

        # 文案
        copy_dir = os.path.join(version_dir, STAGE_DIRS["copy"])
        copy_path = self._find_file(copy_dir, COPY_FILENAMES)

        title_candidates, body, hashtags, full_text = [], "", "", ""
        title = ""
        if copy_path:
            # 尝试中文格式解析，失败则尝试英文格式
            try:
                title_candidates, body, hashtags, full_text = self._parse_copy_cn(copy_path)
            except Exception:
                title_candidates, body, hashtags, full_text = self._parse_copy_en(copy_path)
            selected = [t for t in title_candidates if t.is_selected]
            title = selected[0].text if selected else (
                title_candidates[0].text if title_candidates else ""
            )

        # 策略
        strat_dir = os.path.join(version_dir, STAGE_DIRS["strategy"])
        strategy_path = self._find_file(strat_dir, STRATEGY_FILENAMES)
        pinned_comment = ""
        scheduled_time = None
        if strategy_path:
            pinned_comment, scheduled_time = self._parse_strategy(strategy_path)

        return NoteContent(
            game_name=self.game_name,
            title=title,
            title_candidates=title_candidates,
            body=body,
            hashtags=hashtags,
            full_text=full_text,
            images=images,
            pinned_comment=pinned_comment,
            scheduled_time=scheduled_time,
        )

    # ─── 文案解析（情书格式 - 表格式标题 + 复制用正文）───

    def _parse_copy_cn(self, md_path: str) -> tuple[list[TitleCandidate], str, str, str]:
        content = Path(md_path).read_text(encoding="utf-8")

        # 1. 解析标题候选（表格格式）
        title_candidates = self._parse_title_table(content)

        # 2. 提取"复制用正文"段落
        full_text = self._extract_copy_section(content)

        # 3. 从复制用正文分离标题、正文、hashtag
        body, hashtags = "", ""
        if full_text:
            lines = full_text.strip().split("\n")
            # 最后一行是 hashtag（以 # 开头的连续标签）
            if lines and lines[-1].strip().startswith("#"):
                hashtags = lines[-1].strip()
                body_lines = lines[1:]  # 跳过第一行（标题）
                # 去掉最后一行（hashtag）
                body_lines = body_lines[:-1]
                body = "\n".join(body_lines).strip()
            else:
                body = "\n".join(lines[1:]).strip()
        else:
            # 没有复制用正文段落，从正文段落提取
            body = self._extract_body_section(content)
            hashtags = self._extract_hashtags(content)
            # 组装 full_text
            selected = [t for t in title_candidates if t.is_selected]
            title = selected[0].text if selected else (
                title_candidates[0].text if title_candidates else ""
            )
            parts = [title, "", body]
            if hashtags:
                parts.extend(["", hashtags])
            full_text = "\n".join(parts)

        return title_candidates, body, hashtags, full_text

    def _parse_title_table(self, content: str) -> list[TitleCandidate]:
        """从 Markdown 表格解析标题候选（仅限候选标题段落）"""
        candidates = []

        # 仅截取"候选标题"段落，避免匹配热点适配标题库
        title_section = ""
        m = re.search(
            r"##\s*(?:一、)?候选标题[^#]*?\n([\s\S]+?)(?=\n---|\n##|\Z)",
            content,
        )
        if m:
            title_section = m.group(1)
        else:
            # 回退：取内容前 40 行
            lines = content.split("\n")[:40]
            title_section = "\n".join(lines)

        # 匹配表格行，支持 **加粗** 和 ⭐ 标记
        table_pattern = r"\|\s*\**\s*(悬念型|数字型|共鸣型|反转型)\s*\**\s*(?:⭐)?\s*\|\s*(.+?)\s*\|"
        for m_row in re.finditer(table_pattern, title_section):
            formula = m_row.group(1)
            text = m_row.group(2).strip()
            # 去掉可能的字数列残留
            text = re.sub(r"\s*\|\s*\d+\s*$", "", text)
            candidates.append(TitleCandidate(formula=formula, text=text))

        # 检查"推荐使用"标记
        rec_match = re.search(r"\*\*推荐使用：标题([A-D])\*\*", content)
        if rec_match and candidates:
            idx = ord(rec_match.group(1)) - ord("A")
            if 0 <= idx < len(candidates):
                candidates[idx].is_selected = True

        # 检查 ⭐ 标记
        star_pattern = r"\|\s*\**\s*(悬念型|数字型|共鸣型|反转型)\s*\**\s*⭐"
        star_match = re.search(star_pattern, title_section)
        if star_match and candidates:
            for c in candidates:
                if c.formula == star_match.group(1):
                    c.is_selected = True

        # 检查"推荐标题"代码块
        rec_block = re.search(r"###\s*推荐标题\s*\n```\s*\n(.+?)\n```", content)
        if rec_block and candidates:
            rec_text = rec_block.group(1).strip()
            for c in candidates:
                if c.text.strip() == rec_text.strip():
                    c.is_selected = True

        # 标记第一个为推荐（如果没有其他标记）
        if candidates and not any(c.is_selected for c in candidates):
            candidates[0].is_selected = True

        return candidates

    def _extract_copy_section(self, content: str) -> str:
        """提取"复制用正文"或"发帖复制用正文"段落"""
        text, _ = self._extract_copy_section_typed(content)
        return text

    def _extract_copy_section_typed(self, content: str) -> tuple[str, str]:
        """提取复制用正文段落，返回 (text, type)
        type: "with_title" = 发帖复制用正文（含标题行）
              "body_only" = 完整正文（纯正文）
        """
        # 优先匹配"发帖复制用正文"（含标题）
        for pattern in [
            r"##\s*(?:四、)?发帖复制用正文[^\n]*\n([\s\S]+?)(?=\n## [^#]|\Z)",
            r"##\s*(?:四、)?复制用正文[^\n]*\n([\s\S]+?)(?=\n## [^#]|\Z)",
        ]:
            m = re.search(pattern, content)
            if m:
                text = m.group(1).strip()
                text = re.sub(r"^```\w*\n?", "", text)
                text = re.sub(r"\n?```$", "", text)
                return text.strip(), "with_title"

        # 其次匹配"完整正文"（纯正文，不含标题行）
        for pattern in [
            r"##\s*(?:三、)?完整正文[^\n]*\n([\s\S]+?)(?=\n---|\n## [^#]|\Z)",
        ]:
            m = re.search(pattern, content)
            if m:
                text = m.group(1).strip()
                text = re.sub(r"^```\w*\n?", "", text)
                text = re.sub(r"\n?```$", "", text)
                return text.strip(), "body_only"

        return "", ""

    # ─── 文案解析（UNO 格式 - 标题分节 + 正文分段）───

    def _parse_copy_en(self, md_path: str) -> tuple[list[TitleCandidate], str, str, str]:
        content = Path(md_path).read_text(encoding="utf-8")

        # 1. 解析标题候选（### 标题A/B/C/D 格式）
        title_candidates = self._parse_title_headings(content)

        # 2. 提取正文各段并拼接
        body = self._extract_body_sections_en(content)

        # 3. 提取 hashtag
        hashtags = self._extract_hashtags(content)

        # 4. 组装 full_text
        selected = [t for t in title_candidates if t.is_selected]
        title = selected[0].text if selected else (
            title_candidates[0].text if title_candidates else ""
        )
        parts = [body]
        if hashtags:
            parts.extend(["", hashtags])
        full_text = "\n".join(parts)

        return title_candidates, body, hashtags, full_text

    def _parse_title_headings(self, content: str) -> list[TitleCandidate]:
        """解析 ### 标题A（推荐）格式的标题候选"""
        candidates = []
        # 匹配 "### 标题A（推荐）\n标题文本" 或 "### 标题B\n标题文本"
        pattern = r"###\s*标题([A-D])\s*(?:（(推荐)）)?\s*\n(.+?)(?=\n|$)"
        for m in re.finditer(pattern, content):
            letter = m.group(1)
            is_rec = m.group(2) is not None
            text = m.group(3).strip()
            # 推断公式类型
            formula = self._infer_formula(text)
            candidates.append(TitleCandidate(
                formula=formula, text=text, is_selected=is_rec
            ))

        # 如果没有标记推荐的，检查"推荐使用"行
        if candidates and not any(c.is_selected for c in candidates):
            rec_match = re.search(r"\*\*推荐使用：标题([A-D])\*\*", content)
            if rec_match:
                idx = ord(rec_match.group(1)) - ord("A")
                if 0 <= idx < len(candidates):
                    candidates[idx].is_selected = True

        # 仍然没有推荐的，默认第一个
        if candidates and not any(c.is_selected for c in candidates):
            candidates[0].is_selected = True

        return candidates

    def _infer_formula(self, title: str) -> str:
        """从标题文本推断公式类型"""
        if re.search(r"\d+", title) and any(
            w in title for w in ["款", "个", "步", "分钟", "TOP", "人"]
        ):
            return "数字型"
        if any(w in title for w in ["？", "...", "居然", "竟然", "没想到"]):
            return "悬念型"
        if any(w in title for w in ["以为", "结果", "没想到", "却"]):
            return "反转型"
        if any(w in title for w in ["你", "我们", "不知道", "怎么办"]):
            return "共鸣型"
        return "悬念型"  # 默认

    def _extract_body_sections_en(self, content: str) -> str:
        """提取正文段落并拼接（支持多种段落标题格式）"""
        sections = []
        # 匹配 "### 第N段：XXX" 或 "### 段N：XXX" 后的内容
        pattern = r"###\s*(?:第)?\d+段[：:].+?\n([\s\S]+?)(?=\n###|\n---|\n##|\Z)"
        for m in re.finditer(pattern, content):
            text = m.group(1).strip()
            # 去掉代码块标记
            text = re.sub(r"^```\w*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
            if text:
                sections.append(text.strip())

        if sections:
            return "\n\n".join(sections)

        # 回退：提取 "## 正文" 段落
        m = re.search(r"##\s*正文[\s\S]*?\n([\s\S]+?)(?=\n---|\n##|\Z)", content)
        if m:
            text = m.group(1).strip()
            # 去掉子标题行
            lines = [
                line for line in text.split("\n")
                if not line.strip().startswith("###")
            ]
            return "\n".join(lines).strip()

        return ""

    # ─── 通用文案解析（自动探测格式）───

    def _parse_copy_auto(self, md_path: str) -> tuple[list[TitleCandidate], str, str, str]:
        """自动探测文案格式并解析"""
        content = Path(md_path).read_text(encoding="utf-8")

        # 1. 解析标题候选 - 先尝试表格格式，再尝试标题格式
        title_candidates = self._parse_title_table(content)
        if not title_candidates:
            title_candidates = self._parse_title_headings(content)

        # 2. 提取正文 - 区分"发帖复制用正文"（含标题）和"完整正文"（仅正文）
        copy_text, copy_type = self._extract_copy_section_typed(content)
        body, hashtags = "", ""

        if copy_text:
            lines = copy_text.strip().split("\n")
            # 检测最后一行是否是 hashtag
            last_has_tags = lines and re.search(
                r"(?<![#])#[^#\s]+\s+(?<![#])#[^#\s]+", lines[-1]
            )

            if copy_type == "with_title":
                # "发帖复制用正文" 格式：第一行是标题
                if last_has_tags:
                    hashtags = lines[-1].strip()
                    body = "\n".join(lines[1:-1]).strip()
                else:
                    body = "\n".join(lines[1:]).strip()
            else:
                # "完整正文" 格式：纯正文，不含标题
                if last_has_tags:
                    hashtags = lines[-1].strip()
                    body = "\n".join(lines[:-1]).strip()
                else:
                    body = "\n".join(lines).strip()
        else:
            # 从正文段落提取
            body = self._extract_body_sections_en(content)
            if not body:
                body = self._extract_body_section(content)

        # 3. 如果 hashtags 为空，单独提取
        if not hashtags:
            hashtags = self._extract_hashtags(content)

        # 4. 组装 full_text
        selected = [t for t in title_candidates if t.is_selected]
        title = selected[0].text if selected else (
            title_candidates[0].text if title_candidates else ""
        )
        parts = [body]
        if hashtags:
            parts.extend(["", hashtags])
        full_text = "\n".join(parts)

        return title_candidates, body, hashtags, full_text

    # ─── 通用解析工具 ───

    def _extract_body_section(self, content: str) -> str:
        """提取"正文（6段结构）"段落"""
        m = re.search(
            r"##\s*(?:二、)?正文[^#]*?\n([\s\S]+?)(?=\n---|\n##\s|\Z)",
            content
        )
        return m.group(1).strip() if m else ""

    def _extract_hashtags(self, content: str) -> str:
        """提取 Hashtag 字符串"""
        # 先定位到 Hashtag 段落（用 ## 级别边界，不被 ### 截断）
        hashtag_section = ""
        m = re.search(
            r"##\s*(?:三、|四、)?(?:Hashtag|标签)[^\n]*\n([\s\S]+?)(?=\n## [^#]|\n---\s*\n|\Z)",
            content,
        )
        if m:
            hashtag_section = m.group(1)

        search_text = hashtag_section if hashtag_section else content

        # 从代码块中提取（确保是 XHS 标签而非 Markdown 标题）
        for cb in re.finditer(r"```\s*\n([\s\S]+?)\n```", search_text):
            block = cb.group(1).strip()
            # XHS 标签特征：多个 #单词 连续出现，无 ## 或 ###
            if re.search(r"#[^#\s]+\s+#[^#\s]+", block):
                return block

        # 查找包含多个 XHS 标签的单行（排除表格行）
        for line in search_text.split("\n"):
            line = line.strip()
            if line.startswith("|"):
                continue  # 跳过表格行
            tags = re.findall(r"(?<![#])#([^#\s]+)", line)
            if len(tags) >= 3:
                return line

        # 最终回退：在全文中查找连续多标签行（排除表格）
        if hashtag_section:
            for line in content.split("\n"):
                line = line.strip()
                if line.startswith("|"):
                    continue
                tags = re.findall(r"(?<![#])#([^#\s]+)", line)
                if len(tags) >= 3:
                    return line

        return ""

    def _parse_strategy(self, md_path: str) -> tuple[str, str | None]:
        """解析发帖策略文件，提取置顶评论和发布时间建议"""
        content = Path(md_path).read_text(encoding="utf-8")

        # 提取置顶评论
        pinned = ""
        # 查找 > 引用块中的置顶评论
        m = re.search(r"置顶评论.*?\n(?:.*\n)*?>\s*(.+?)(?:\n\n|\n>|\Z)", content)
        if m:
            pinned = m.group(1).strip()
        else:
            # 查找代码块中的置顶评论
            m = re.search(r"置顶评论[\s\S]*?```\s*\n([\s\S]+?)\n```", content)
            if m:
                pinned = m.group(1).strip()

        # 提取发布时间建议（简化为描述文本）
        scheduled = None
        time_patterns = [
            r"(周[一二三四五六日]\s*\d{1,2}:\d{2})",
            r"(\d{1,2}:\d{2}[-–]\d{1,2}:\d{2})",
            r"((?:节前|清明前)\s*\d+-\d+天)",
        ]
        for pattern in time_patterns:
            m = re.search(pattern, content)
            if m:
                scheduled = m.group(1)
                break

        return pinned, scheduled

    def _find_file(self, directory: str, candidates: list[str]) -> str | None:
        """在目录中查找候选文件名"""
        if not directory or not os.path.isdir(directory):
            return None
        for name in candidates:
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                return path
        return None


def main():
    """CLI 入口：python publisher/parser.py --project <项目名>"""
    import argparse

    parser = argparse.ArgumentParser(description="桌游项目内容解析器")
    parser.add_argument("--project", required=True, help="项目名称（如 情书、uno）")
    parser.add_argument("--root", default=PROJECT_ROOT, help="项目根目录")
    args = parser.parse_args()

    project_path = os.path.join(args.root, args.project)
    try:
        p = ProjectParser(project_path)
        fmt = p.detect_format()
        print(f"检测到格式: {fmt}", file=sys.stderr)
        content = p.parse()
        print(content.to_json())
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
