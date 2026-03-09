"""笔记装配器 - 将解析内容组合为发布就绪版本"""

from __future__ import annotations

import json
import os
import sys

from publisher.config import PROJECT_ROOT
from publisher.models import ImageAsset, NoteContent, PublishVersion


class NoteAssembler:
    """笔记装配器 - 组合图片序列+文案为发布版本"""

    def __init__(self, content: NoteContent):
        self.content = content

    def assemble_default(self) -> PublishVersion:
        """按推荐方案装配默认版本"""
        cover = self._select_default_cover()
        title_candidate = self._select_default_title()

        return PublishVersion(
            version_id=f"default_{cover.role}",
            cover=cover,
            title=title_candidate.text,
            title_formula=title_candidate.formula,
            body=self.content.body,
            hashtags=self.content.hashtags,
            image_sequence=self._build_image_sequence(cover),
        )

    def assemble_version(
        self,
        cover_choice: str | None = None,
        title_index: int | None = None,
    ) -> PublishVersion:
        """按指定封面和标题组合装配版本

        Args:
            cover_choice: 封面选择 "A"/"B"/"C" 或 None(使用推荐)
            title_index: 标题索引 0-3 或 None(使用推荐)
        """
        # 选择封面
        if cover_choice:
            cover = self._select_cover_by_letter(cover_choice.upper())
        else:
            cover = self._select_default_cover()

        # 选择标题
        if title_index is not None and 0 <= title_index < len(self.content.title_candidates):
            tc = self.content.title_candidates[title_index]
        else:
            tc = self._select_default_title()

        cover_letter = cover.role.split("_")[1] if "_" in cover.role else "x"
        version_id = f"cover{cover_letter}_title{title_index or 0}"

        return PublishVersion(
            version_id=version_id,
            cover=cover,
            title=tc.text,
            title_formula=tc.formula,
            body=self.content.body,
            hashtags=self.content.hashtags,
            image_sequence=self._build_image_sequence(cover),
        )

    def assemble_ab_versions(self) -> list[PublishVersion]:
        """生成 A/B 测试的所有版本组合"""
        versions = []
        covers = self.content.get_covers()
        titles = self.content.title_candidates

        if not covers or not titles:
            # 至少返回默认版本
            return [self.assemble_default()]

        # 推荐的标题
        selected_title = self._select_default_title()
        selected_idx = 0
        for i, t in enumerate(titles):
            if t.is_selected:
                selected_idx = i
                break

        # 封面优先级: B(高点击率) > A(文艺) > C(人物)
        cover_priority = ["cover_b", "cover_a", "cover_c"]
        sorted_covers = sorted(
            covers,
            key=lambda c: (
                cover_priority.index(c.role)
                if c.role in cover_priority
                else len(cover_priority)
            ),
        )

        # Round 1: 每个封面 × 推荐标题
        for i, cover in enumerate(sorted_covers):
            cover_letter = cover.role.split("_")[1].upper() if "_" in cover.role else "X"
            versions.append(PublishVersion(
                version_id=f"round{i+1}_cover{cover_letter}_title{selected_idx}",
                cover=cover,
                title=selected_title.text,
                title_formula=selected_title.formula,
                body=self.content.body,
                hashtags=self.content.hashtags,
                image_sequence=self._build_image_sequence(cover),
            ))

        # Round 2: 推荐封面 × 其他标题（最多 2 个额外版本）
        best_cover = sorted_covers[0] if sorted_covers else covers[0]
        for i, tc in enumerate(titles):
            if i == selected_idx:
                continue
            if len(versions) >= 6:  # 最多 6 个版本
                break
            cover_letter = best_cover.role.split("_")[1].upper() if "_" in best_cover.role else "X"
            versions.append(PublishVersion(
                version_id=f"round{len(versions)+1}_cover{cover_letter}_title{i}",
                cover=best_cover,
                title=tc.text,
                title_formula=tc.formula,
                body=self.content.body,
                hashtags=self.content.hashtags,
                image_sequence=self._build_image_sequence(best_cover),
            ))

        return versions

    def _build_image_sequence(self, cover: ImageAsset) -> list[ImageAsset]:
        """构建完整的图片发布序列"""
        sequence = []

        # 1. 封面（order=1）
        cover_copy = ImageAsset(
            path=cover.path, role=cover.role,
            label=cover.label, order=1,
        )
        sequence.append(cover_copy)

        # 2. 内页（order=2~5）
        sequence.extend(self.content.get_inner_pages())

        # 3. 规则图（order=6，如果有的话）
        rule_graphics = self.content.get_rule_graphics()
        if rule_graphics:
            # 优先使用极简版
            rg = rule_graphics[0]
            for r in rule_graphics:
                if "极简" in r.label:
                    rg = r
                    break
            sequence.append(rg)

        return sorted(sequence, key=lambda x: x.order)

    def _select_default_cover(self) -> ImageAsset:
        """选择默认封面（优先 B 线高点击率）"""
        covers = self.content.get_covers()
        if not covers:
            raise ValueError("项目中未找到封面图片")

        for priority in ["cover_b", "cover_a", "cover_c"]:
            for c in covers:
                if c.role == priority:
                    return c
        return covers[0]

    def _select_cover_by_letter(self, letter: str) -> ImageAsset:
        """按字母选择封面"""
        role = f"cover_{letter.lower()}"
        for img in self.content.get_covers():
            if img.role == role:
                return img
        raise ValueError(f"未找到封面 {letter}，可用: {[c.role for c in self.content.get_covers()]}")

    def _select_default_title(self):
        """选择默认标题（推荐的或第一个）"""
        if not self.content.title_candidates:
            from publisher.models import TitleCandidate
            return TitleCandidate(formula="", text=self.content.title)

        for t in self.content.title_candidates:
            if t.is_selected:
                return t
        return self.content.title_candidates[0]

    def get_summary(self, version: PublishVersion) -> str:
        """生成版本摘要（用于展示给用户）"""
        lines = [
            f"## 发布版本: {version.version_id}",
            "",
            f"**标题**: {version.title}",
            f"**标题公式**: {version.title_formula}",
            f"**封面**: {version.cover.label}",
            f"**图片数量**: {len(version.image_sequence)} 张",
            "",
            "**图片序列**:",
        ]
        for img in sorted(version.image_sequence, key=lambda x: x.order):
            lines.append(f"  {img.order}. {img.label} ({os.path.basename(img.path)})")

        lines.extend([
            "",
            f"**正文字数**: {len(version.body)} 字",
            f"**Hashtag**: {version.hashtags[:60]}...",
        ])

        return "\n".join(lines)


def main():
    """CLI 入口"""
    import argparse
    from publisher.parser import ProjectParser

    ap = argparse.ArgumentParser(description="桌游笔记装配器")
    ap.add_argument("--project", required=True, help="项目名称")
    ap.add_argument("--root", default=PROJECT_ROOT, help="项目根目录")
    ap.add_argument("--cover", default=None, help="封面选择: A/B/C")
    ap.add_argument("--title", type=int, default=None, help="标题索引: 0-3")
    ap.add_argument("--ab", action="store_true", help="生成所有A/B测试版本")
    args = ap.parse_args()

    project_path = os.path.join(args.root, args.project)
    parser = ProjectParser(project_path)
    content = parser.parse()
    assembler = NoteAssembler(content)

    if args.ab:
        versions = assembler.assemble_ab_versions()
        result = [v.to_dict() for v in versions]
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        version = assembler.assemble_version(args.cover, args.title)
        print(version.to_json())
        print("\n---\n", file=sys.stderr)
        print(assembler.get_summary(version), file=sys.stderr)


if __name__ == "__main__":
    main()
