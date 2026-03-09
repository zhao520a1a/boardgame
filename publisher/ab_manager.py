"""A/B 测试版本管理器"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from publisher.config import PROJECT_ROOT, PUBLISH_HISTORY_DIR
from publisher.models import NoteContent, PublishVersion


class ABTestManager:
    """A/B 测试版本管理 - 生成/选择/切换/记录测试版本"""

    def __init__(self, project_root: str, versions: list[PublishVersion] | None = None):
        self.project_root = os.path.abspath(project_root)
        self.history_dir = os.path.join(self.project_root, PUBLISH_HISTORY_DIR)
        self.versions_file = os.path.join(self.history_dir, "ab_versions.json")
        self.versions = versions or []
        self._ensure_dir()

    def _ensure_dir(self):
        os.makedirs(self.history_dir, exist_ok=True)

    def save_versions(self):
        """保存版本列表到文件"""
        data = {
            "game_name": os.path.basename(self.project_root),
            "created_at": datetime.now().isoformat(),
            "versions": [v.to_dict() for v in self.versions],
        }
        Path(self.versions_file).write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def load_versions(self) -> list[PublishVersion]:
        """从文件加载版本列表"""
        if not os.path.isfile(self.versions_file):
            return []
        data = json.loads(Path(self.versions_file).read_text(encoding="utf-8"))
        self.versions = [
            PublishVersion.from_dict(v) for v in data.get("versions", [])
        ]
        return self.versions

    def get_current_version(self) -> PublishVersion | None:
        """获取当前待发布的版本（第一个 pending 状态的）"""
        for v in self.versions:
            if v.status == "pending":
                return v
        return None

    def get_published_versions(self) -> list[PublishVersion]:
        """获取已发布的版本列表"""
        return [v for v in self.versions if v.status in ("published", "evaluated")]

    def mark_published(self, version_id: str):
        """标记版本为已发布"""
        for v in self.versions:
            if v.version_id == version_id:
                v.status = "published"
                break
        self.save_versions()

    def record_metrics(self, version_id: str, metrics: dict):
        """记录版本的效果数据"""
        for v in self.versions:
            if v.version_id == version_id:
                v.status = "evaluated"
                break
        self.save_versions()

    def advance_to_next(self, reason: str = "") -> PublishVersion | None:
        """切换到下一个待测试版本"""
        next_version = self.get_current_version()
        return next_version

    def get_status_report(self) -> str:
        """生成 Markdown 格式的状态汇总"""
        lines = [
            f"# A/B 测试状态 - {os.path.basename(self.project_root)}",
            "",
            f"总版本数: {len(self.versions)}",
            "",
            "| 版本ID | 封面 | 标题公式 | 状态 |",
            "|--------|------|---------|------|",
        ]

        for v in self.versions:
            status_icon = {
                "pending": "⏳",
                "published": "📤",
                "evaluated": "📊",
            }.get(v.status, "❓")
            title_short = v.title[:20] + "..." if len(v.title) > 20 else v.title
            lines.append(
                f"| {v.version_id} | {v.cover.label} | {v.title_formula} | {status_icon} {v.status} |"
            )

        published = self.get_published_versions()
        pending = [v for v in self.versions if v.status == "pending"]
        lines.extend([
            "",
            f"已发布: {len(published)} / 待测试: {len(pending)}",
        ])

        next_v = self.get_current_version()
        if next_v:
            lines.extend([
                "",
                f"**下一个版本**: {next_v.version_id}",
                f"- 封面: {next_v.cover.label}",
                f"- 标题: {next_v.title}",
            ])

        return "\n".join(lines)


def main():
    """CLI 入口"""
    import argparse

    ap = argparse.ArgumentParser(description="A/B 测试版本管理")
    ap.add_argument("--project", required=True, help="项目名称")
    ap.add_argument("--root", default=PROJECT_ROOT, help="项目根目录")
    ap.add_argument(
        "--action",
        choices=["status", "next", "init"],
        default="status",
        help="操作: status(查看状态) / next(切换下一版本) / init(初始化)",
    )
    args = ap.parse_args()

    project_path = os.path.join(args.root, args.project)
    manager = ABTestManager(project_path)

    if args.action == "init":
        from publisher.assembler import NoteAssembler
        from publisher.parser import ProjectParser

        parser = ProjectParser(project_path)
        content = parser.parse()
        assembler = NoteAssembler(content)
        versions = assembler.assemble_ab_versions()
        manager.versions = versions
        manager.save_versions()
        print(f"已初始化 {len(versions)} 个 A/B 测试版本")
        print(manager.get_status_report())

    elif args.action == "status":
        manager.load_versions()
        print(manager.get_status_report())

    elif args.action == "next":
        manager.load_versions()
        next_v = manager.advance_to_next()
        if next_v:
            print(f"下一个版本: {next_v.version_id}")
            print(json.dumps(next_v.to_dict(), ensure_ascii=False, indent=2))
        else:
            print("所有版本已测试完毕")


if __name__ == "__main__":
    main()
