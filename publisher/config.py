"""配置常量 - 小红书发布系统"""

import os

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 小红书创作者平台 URL
XHS_CREATOR_URL = "https://creator.xiaohongshu.com/publish/publish"

# 输出目录名称（两种命名风格）
OUTPUT_DIR_NAMES = ["输出", "output"]

# 版本目录正则模式
VERSION_DIR_PATTERN = r"^v(\d+)_(\d{4})$"

# 各阶段子目录名称映射
STAGE_DIRS = {
    "input": "01_input-collection",
    "rule": "02_rule-graphic",
    "cover": "03_cover-design",
    "inner": "04_inner-pages",
    "copy": "05_copywriting",
    "strategy": "06_posting-strategy",
    "publish": "07_publishing",
}

# 图片角色定义
IMAGE_ROLES = {
    "cover_a": {"label": "封面A_文艺调性", "order": 1},
    "cover_b": {"label": "封面B_高点击率", "order": 1},
    "cover_c": {"label": "封面C_人物产品", "order": 1},
    "inner_p2": {"label": "教学页", "order": 2},
    "inner_p3": {"label": "解析页", "order": 3},
    "inner_p4": {"label": "场景页", "order": 4},
    "inner_p5": {"label": "技巧页", "order": 5},
    "rule_graphic": {"label": "规则速查图", "order": 6},
}

# 封面文件名匹配模式（中文命名风格 - 情书项目）
COVER_PATTERNS_CN = {
    "cover_a": ["封面A", "封面a"],
    "cover_b": ["封面B", "封面b"],
    "cover_c": ["封面C", "封面c"],
}

# 内页文件名匹配模式（中文命名风格 - 情书项目）
INNER_PATTERNS_CN = {
    "inner_p2": ["内页1", "P2"],
    "inner_p3": ["内页2", "P3"],
    "inner_p4": ["内页3", "P4"],
    "inner_p5": ["内页4", "P5"],
}

# 规则图文件名匹配
RULE_GRAPHIC_PATTERNS = ["规则速查图", "规则图", "rule"]

# 文案文件名候选
COPY_FILENAMES = ["文案.md", "文案完整版.md", "final-copy.md"]

# 策略文件名候选
STRATEGY_FILENAMES = ["发帖策略.md", "posting-strategy.md"]

# 发布历史目录名
PUBLISH_HISTORY_DIR = "publish_history"

# 标题公式类型
TITLE_FORMULAS = ["悬念型", "数字型", "共鸣型", "反转型"]
