"""数据结构定义 - 小红书发布系统核心模型"""

from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ImageAsset:
    """图片资产"""

    path: str  # 文件绝对路径
    role: str  # cover_a, cover_b, cover_c, inner_p2~p5, rule_graphic
    label: str  # 人类可读标签（如"封面A_文艺调性"）
    order: int = 0  # 在笔记中的排列顺序

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> ImageAsset:
        return cls(**data)


@dataclass
class TitleCandidate:
    """标题候选"""

    formula: str  # 公式类型：悬念型/数字型/共鸣型/反转型
    text: str  # 标题文本
    is_selected: bool = False  # 是否为推荐标题

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> TitleCandidate:
        return cls(**data)


@dataclass
class NoteContent:
    """归一化后的笔记内容（解析器产出）"""

    game_name: str
    title: str  # 选定标题
    title_candidates: list[TitleCandidate] = field(default_factory=list)
    body: str = ""  # 正文（不含标题和 hashtag）
    hashtags: str = ""  # Hashtag 字符串
    full_text: str = ""  # 完整复制用文本（标题+正文+hashtag）
    images: list[ImageAsset] = field(default_factory=list)
    pinned_comment: str = ""  # 置顶评论话术
    scheduled_time: Optional[str] = None  # 推荐发布时间描述

    def get_covers(self) -> list[ImageAsset]:
        """获取所有封面图"""
        return [img for img in self.images if img.role.startswith("cover")]

    def get_inner_pages(self) -> list[ImageAsset]:
        """获取所有内页图（按 order 排序）"""
        pages = [img for img in self.images if img.role.startswith("inner")]
        return sorted(pages, key=lambda x: x.order)

    def get_rule_graphics(self) -> list[ImageAsset]:
        """获取规则图"""
        return [img for img in self.images if img.role == "rule_graphic"]

    def to_dict(self) -> dict:
        return {
            "game_name": self.game_name,
            "title": self.title,
            "title_candidates": [t.to_dict() for t in self.title_candidates],
            "body": self.body,
            "hashtags": self.hashtags,
            "full_text": self.full_text,
            "images": [img.to_dict() for img in self.images],
            "pinned_comment": self.pinned_comment,
            "scheduled_time": self.scheduled_time,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    @classmethod
    def from_dict(cls, data: dict) -> NoteContent:
        return cls(
            game_name=data["game_name"],
            title=data["title"],
            title_candidates=[
                TitleCandidate.from_dict(t) for t in data.get("title_candidates", [])
            ],
            body=data.get("body", ""),
            hashtags=data.get("hashtags", ""),
            full_text=data.get("full_text", ""),
            images=[ImageAsset.from_dict(img) for img in data.get("images", [])],
            pinned_comment=data.get("pinned_comment", ""),
            scheduled_time=data.get("scheduled_time"),
        )


@dataclass
class PublishVersion:
    """A/B 测试发布版本"""

    version_id: str
    cover: ImageAsset
    title: str
    title_formula: str  # 标题公式类型
    body: str
    hashtags: str
    image_sequence: list[ImageAsset] = field(default_factory=list)
    scheduled_time: Optional[str] = None
    status: str = "pending"  # pending / published / evaluated

    def get_full_text(self) -> str:
        """组合完整发布文本（正文+hashtag，标题单独填）"""
        parts = [self.body]
        if self.hashtags:
            parts.append("")
            parts.append(self.hashtags)
        return "\n".join(parts)

    def get_image_paths(self) -> list[str]:
        """获取排序后的图片绝对路径列表"""
        return [img.path for img in sorted(self.image_sequence, key=lambda x: x.order)]

    def to_dict(self) -> dict:
        return {
            "version_id": self.version_id,
            "cover": self.cover.to_dict(),
            "title": self.title,
            "title_formula": self.title_formula,
            "body": self.body,
            "hashtags": self.hashtags,
            "image_sequence": [img.to_dict() for img in self.image_sequence],
            "scheduled_time": self.scheduled_time,
            "status": self.status,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    @classmethod
    def from_dict(cls, data: dict) -> PublishVersion:
        return cls(
            version_id=data["version_id"],
            cover=ImageAsset.from_dict(data["cover"]),
            title=data["title"],
            title_formula=data.get("title_formula", ""),
            body=data.get("body", ""),
            hashtags=data.get("hashtags", ""),
            image_sequence=[
                ImageAsset.from_dict(img)
                for img in data.get("image_sequence", [])
            ],
            scheduled_time=data.get("scheduled_time"),
            status=data.get("status", "pending"),
        )


@dataclass
class PublishLog:
    """发布日志记录"""

    log_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    game_name: str = ""
    version_id: str = ""
    publish_time: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )
    status: str = "prepared"  # prepared / filled / published / scheduled / failed
    platform: str = "xiaohongshu"
    title_used: str = ""
    title_formula: str = ""
    cover_style: str = ""  # A_文艺调性 / B_高点击率 / C_人物产品
    image_count: int = 0
    image_labels: list[str] = field(default_factory=list)
    hashtag_count: int = 0
    body_char_count: int = 0
    screenshot_pre: Optional[str] = None
    screenshot_post: Optional[str] = None
    note_url: Optional[str] = None
    ab_round: int = 1
    metrics: dict = field(default_factory=dict)  # ctr, likes, saves, comments
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    @classmethod
    def from_dict(cls, data: dict) -> PublishLog:
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
