---
name: boardgame-cover-design
description: "桌游笔记封面图生成。提供3条风格线（文艺调性/高点击率/人物产品），根据推广目标生成3张不同风格封面供A/B测试。当用户需要生成桌游封面、小红书封面、笔记首图时调用。关键词：封面设计、风格线、A/B测试、小红书封面。"
---

# 封面图生成

> 职责：根据风格线生成 3 张高质量封面，支持 A/B 测试选优。

## 输入要求

从上下文摘要中获取：
- 游戏名称（中英文）
- 核心机制关键词
- 人数/时长
- 推广目标
- 风格线选择
- 参考素材描述

## 通用设计规范

所有封面必须满足：

| 规范 | 要求 |
|------|------|
| 尺寸 | 3:4 比例（768x1024） |
| 标题文字 | 占画面 30-40%，缩略图必须可读 |
| 必含元素 | 游戏名（中+英）、核心卖点标签（人数/时长） |
| 设计原则 | 情绪钩子 > 信息传递（先抓眼球再讲内容） |
| 好奇缺口 | 每张留一个驱动点击的悬念 |
| 文字语言 | 图片中所有文字必须是清晰可见的汉字（中文），禁止出现英文文字 |

## 三条风格线

### A 线：文艺调性（适合文艺号/种草安利）

| 子风格 | 视觉关键词 | 色调 | 适合类型 |
|--------|-----------|------|---------|
| 日系手作 | 胶片感、自然光、木桌、咖啡干花 | 暖棕米色 | 策略/拼图/安静类 |
| 平铺美学 | 俯拍 knolling、亚麻底布、精致摆拍 | 莫兰迪色系 | 组件精美的游戏 |
| 烛光夜话 | 暖光、fairy light、小团体互动 | 金色暖调 | 双人/社交/情感类 |

**A 线 Prompt 模板**：
```
A beautifully styled flat-lay photograph of the board game "[游戏名]".
[子风格视觉描述]. Warm [色调] color palette.
Game components artfully arranged on [材质背景].
Soft natural lighting, film grain texture, KINFOLK magazine aesthetic.
Text overlay: "[游戏中文名]" in elegant serif font, "[卖点标签]".
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, lifestyle photography.
```

### B 线：高点击率（适合涨粉/冲流量）

| 子风格 | 核心钩子 | 视觉手法 | 适合类型 |
|--------|---------|---------|---------|
| 悬念钩子 | 好奇心缺口（「千万别...」） | 暗调电影感、关键瞬间特写 | 有爆炸/反转机制的 |
| 情绪冲击 | 表情包级感染力 + 金句 | 夸张表情大特写、高饱和 | 有戏剧性结局的 |
| 对比反差 | 戏剧反差驱动停留 | 分屏 before/after、冷暖色对撞 | 有大起大落的 |

**B 线 Prompt 模板**：
```
A dramatic, high-impact social media cover for board game "[游戏名]".
[子风格视觉描述]. Bold cinematic lighting with [色调对比].
[场景描述：紧张瞬间/夸张表情/对比画面].
Large bold text: "[悬念标题]" in impactful sans-serif font.
Tag line: "[人数] | [时长]". High saturation, attention-grabbing.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, social media optimized.
```

### C 线：人物产品（适合带货/品牌合作）

| 子风格 | 构图 | 视觉重点 |
|--------|------|---------|
| 博主推荐 | 人物手持游戏盒 + 大字标签 | 信任感、真实感 |
| 聚会实拍 | 多人围桌、自然互动 | 社交氛围、场景代入 |

**C 线 Prompt 模板**：
```
A lifestyle product shot featuring the board game "[游戏名]".
[人物手持游戏盒/多人围桌游戏场景].
Natural candid interaction, warm ambient lighting.
Product clearly visible with game name. Styled text labels.
Authentic social gathering atmosphere.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, product photography.
```

## 执行流程

### 1. 确定风格组合

根据推广目标和用户偏好，选择 3 张封面的风格组合：

| 用户选择 | 生成组合 |
|---------|---------|
| 文艺调性 | A 线 3 个子风格各 1 张 |
| 高点击率 | B 线 3 个子风格各 1 张 |
| 人物产品 | C 线 2 个子风格 + B 线 1 个悬念钩子 |
| 全部都来 | A/B/C 各 1 张最佳子风格 |

### 2. 构建 Prompt 并生成

- 基于模板填充具体游戏信息
- 使用 `ImageGen` 工具生成，尺寸 768x1024
- 图片保存到游戏对应目录

### 3. 输出与确认

展示 3 张封面，附上：
- 每张的风格线标签
- 适用场景说明
- 建议用户选定 1 张作为主封面
