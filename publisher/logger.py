"""发布日志 - 记录和查询发布历史"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from publisher.config import PROJECT_ROOT, PUBLISH_HISTORY_DIR
from publisher.models import PublishLog, PublishVersion


class PublishLogger:
    """发布日志管理 - 记录每次发布的内容组合、时间、状态"""

    def __init__(self, project_root: str):
        self.project_root = os.path.abspath(project_root)
        self.history_dir = os.path.join(self.project_root, PUBLISH_HISTORY_DIR)
        os.makedirs(self.history_dir, exist_ok=True)

    def create_entry(self, version: PublishVersion, status: str = "prepared") -> PublishLog:
        """创建新的发布日志条目"""
        now = datetime.now()
        log = PublishLog(
            game_name=os.path.basename(self.project_root),
            version_id=version.version_id,
            publish_time=now.isoformat(),
            status=status,
            title_used=version.title,
            title_formula=version.title_formula,
            cover_style=version.cover.label,
            image_count=len(version.image_sequence),
            image_labels=[img.label for img in version.image_sequence],
            hashtag_count=version.hashtags.count("#"),
            body_char_count=len(version.body),
        )
        self._save_log(log)
        return log

    def update_status(self, log_id: str, status: str, **kwargs):
        """更新日志状态"""
        log = self._load_log_by_id(log_id)
        if not log:
            raise ValueError(f"未找到日志: {log_id}")
        log.status = status
        for k, v in kwargs.items():
            if hasattr(log, k):
                setattr(log, k, v)
        self._save_log(log)
        return log

    def update_metrics(self, log_id: str, metrics: dict):
        """追加效果数据"""
        log = self._load_log_by_id(log_id)
        if not log:
            raise ValueError(f"未找到日志: {log_id}")
        log.metrics.update(metrics)
        log.metrics["updated_at"] = datetime.now().isoformat()
        self._save_log(log)
        return log

    def get_history(self) -> list[PublishLog]:
        """获取所有发布日志"""
        logs = []
        for fname in sorted(os.listdir(self.history_dir)):
            if fname.endswith(".json") and fname != "ab_versions.json":
                fpath = os.path.join(self.history_dir, fname)
                try:
                    data = json.loads(Path(fpath).read_text(encoding="utf-8"))
                    logs.append(PublishLog.from_dict(data))
                except (json.JSONDecodeError, KeyError):
                    continue
        return logs

    def generate_report(self) -> str:
        """生成 Markdown 格式的发布历史汇总"""
        logs = self.get_history()
        game = os.path.basename(self.project_root)

        lines = [
            f"# 发布历史 - {game}",
            "",
            f"总发布次数: {len(logs)}",
            "",
        ]

        if not logs:
            lines.append("暂无发布记录。")
            return "\n".join(lines)

        lines.extend([
            "| 时间 | 版本 | 标题 | 封面 | 状态 |",
            "|------|------|------|------|------|",
        ])

        for log in logs:
            time_short = log.publish_time[:16].replace("T", " ")
            title_short = log.title_used[:15] + "..." if len(log.title_used) > 15 else log.title_used
            status_icon = {
                "prepared": "📝",
                "filled": "📋",
                "published": "✅",
                "scheduled": "⏰",
                "failed": "❌",
            }.get(log.status, "❓")
            lines.append(
                f"| {time_short} | {log.version_id} | {title_short} | {log.cover_style} | {status_icon} {log.status} |"
            )

        # 效果数据汇总
        evaluated = [l for l in logs if l.metrics]
        if evaluated:
            lines.extend([
                "",
                "## 效果数据",
                "",
                "| 版本 | 点赞 | 收藏 | 评论 | CTR |",
                "|------|------|------|------|-----|",
            ])
            for log in evaluated:
                m = log.metrics
                lines.append(
                    f"| {log.version_id} | {m.get('likes', '-')} | "
                    f"{m.get('saves', '-')} | {m.get('comments', '-')} | "
                    f"{m.get('ctr', '-')} |"
                )

        return "\n".join(lines)

    def _save_log(self, log: PublishLog):
        """保存单条日志"""
        # 用 log_id 作为文件名
        fpath = os.path.join(self.history_dir, f"log_{log.log_id}.json")
        Path(fpath).write_text(log.to_json(), encoding="utf-8")

    def _load_log_by_id(self, log_id: str) -> PublishLog | None:
        """按 ID 加载日志"""
        fpath = os.path.join(self.history_dir, f"log_{log_id}.json")
        if os.path.isfile(fpath):
            data = json.loads(Path(fpath).read_text(encoding="utf-8"))
            return PublishLog.from_dict(data)
        # 遍历查找
        for fname in os.listdir(self.history_dir):
            if fname.endswith(".json") and fname != "ab_versions.json":
                fpath = os.path.join(self.history_dir, fname)
                try:
                    data = json.loads(Path(fpath).read_text(encoding="utf-8"))
                    if data.get("log_id") == log_id:
                        return PublishLog.from_dict(data)
                except (json.JSONDecodeError, KeyError):
                    continue
        return None


def main():
    """CLI 入口"""
    import argparse

    ap = argparse.ArgumentParser(description="发布日志管理")
    ap.add_argument("--project", required=True, help="项目名称")
    ap.add_argument("--root", default=PROJECT_ROOT, help="项目根目录")
    ap.add_argument(
        "--action",
        choices=["history", "report"],
        default="report",
        help="操作: history(JSON) / report(Markdown)",
    )
    args = ap.parse_args()

    project_path = os.path.join(args.root, args.project)
    logger = PublishLogger(project_path)

    if args.action == "history":
        logs = logger.get_history()
        result = [l.to_dict() for l in logs]
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(logger.generate_report())


if __name__ == "__main__":
    main()
