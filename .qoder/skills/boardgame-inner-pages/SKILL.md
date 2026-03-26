---
name: boardgame-inner-pages
description: "桌游笔记内页图生成。默认生成2张内页（教学页/技巧页），可选生成解析页和场景页，构成完整滑动阅读体验，风格与封面统一。当用户需要生成桌游笔记内页、图文内容页、小红书滑动图时调用。关键词：内页设计、教学图、场景图、技巧图、滑动图。"
---

# 内页图生成

> 职责：生成 P2、P5 共 2 张内页（默认），与封面（P1）构成 3P 滑动阅读体验。可选生成 P3、P4。

## 输入要求

从上下文摘要及前序阶段获取：
- 游戏名称、核心机制、规则摘要
- 已选定的封面风格线及配色
- 参考素材描述

## 内页结构

| 页码 | 类型 | 内容 | 核心目的 | 默认状态 |
|------|------|------|---------|---------|
| P1 | 封面 | （来自 cover-design） | 吸引点击 | 必选 |
| P2 | 教学页 | N 步学会 / 快速教学 | 降低门槛 | **默认生成** |
| P3 | 解析页 | 为什么好玩 / 核心刺激点 | 激发兴趣 | **默认跳过** |
| P4 | 场景页 | 真实游戏场景 | 场景代入 | **默认跳过** |
| P5 | 技巧页 | 进阶技巧 / 隐藏玩法 | 驱动收藏 | **默认生成** |

> **默认生成逻辑**：P2（教学页）和 P5（技巧页）为必选页面；P3（解析页）和 P4（场景页）默认跳过，如需生成请明确指定。

## 各页设计规范

### P2：教学页

**设计原则**：让完全不懂的人 10 秒看懂核心玩法。

- 步骤数：3-5 步，不超过 5 步
- 排版：编号卡片式 / 流程图式
- 图标驱动：每步配一个直觉图标
- 文字极简：每步不超过 15 字
- 遵循黄金三步：主题代入 → 获胜条件 → 核心行动

**Prompt 模板**：
```
A clean infographic teaching card for board game "[游戏名]".
[N] numbered steps with icons, card-style layout.
Step 1: [步骤描述]. Step 2: [步骤描述]. ...
[配色方案] color scheme matching the cover style.
Clean white/light background, modern flat design icons.
Large readable text, step-by-step tutorial format.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, educational infographic.
```

### P3：解析页（可选）

> ⚠️ **默认跳过**，如需生成请明确指定。

**设计原则**：传递「这游戏为什么让人上瘾」的核心体验。

- 聚焦 1-2 个核心刺激点（不贪多）
- 可视化机制：用图解/对比/数据替代文字
- 制造「想玩」冲动：强调决策张力、反转刺激、社交互动
- 可用手法：概率对比图、决策树、玩家心理博弈图解

**Prompt 模板**：
```
An engaging analytical graphic for board game "[游戏名]".
Visualizing the core excitement: [核心刺激点描述].
[图解类型：probability chart / decision tree / vs comparison].
Dynamic layout with [配色方案], highlighting tension and fun.
Bold accent colors for key moments. Minimal text, visual-first.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, data visualization style.
```

### P4：场景页（可选）

> ⚠️ **默认跳过**，如需生成请明确指定。

**设计原则**：让用户代入「我也想这样玩」的场景感。

- 真实感 > 摆拍感
- 必须有人物互动（表情、动作、氛围）
- 场景类型根据推广目标选择：

| 推广目标 | 推荐场景 |
|---------|---------|
| 涨粉 | 聚会欢笑、夸张反应 |
| 种草 | 咖啡馆/家居温馨桌游时光 |
| 带货 | 产品特写 + 使用场景组合 |

**Prompt 模板**：
```
A lifestyle photograph of people playing "[游戏名]".
[场景描述：cozy living room / cafe gathering / party night].
Natural candid moments, genuine laughter and interaction.
Warm ambient lighting, [配色调性].
Game components visible on table. Authentic social atmosphere.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, lifestyle photography.
```

### P5：技巧页

**设计原则**：制造「收藏价值」，让用户保存笔记。

- 标题用收藏钩子：
  - 「老玩家偷偷在用的 3 个技巧」
  - 「99% 的人不知道的隐藏玩法」
  - 「看完多赢 30% 的进阶攻略」
- 内容：2-4 个实用技巧，编号卡片式
- 每个技巧：标题 + 一句话说明 + 图标
- 底部可加互动引导：「你还发现了什么技巧？评论区分享」

**Prompt 模板**：
```
A tips and tricks card for board game "[游戏名]".
Title: "[收藏钩子标题]".
[N] pro tips in numbered card format with icons.
Tip 1: [技巧]. Tip 2: [技巧]. ...
[配色方案] matching cover style. Premium card design feel.
Call-to-action at bottom. Collectible reference card aesthetic.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, strategy guide design.
```

## 通用设计规范

所有内页必须满足：

| 规范 | 要求 |
|------|------|
| 尺寸 | 768x1024（3:4） |
| 风格一致性 | 色系、字体、装饰元素与封面统一 |
| 留白 | >= 20% |
| 字体 | >= 10pt，高对比度 |
| 可视化优先 | 图标/流程图 > 文字段落 |
| 文字语言 | 图片中所有文字必须是清晰可见的汉字（中文），禁止出现英文文字 |

## 执行流程

1. **规则图生成**（默认调用）：
   - 调用 `/boardgame-rule-graphic` 生成规则讲解图
   - 输出：AI生成风格图 + HTML信息图双轨产物

2. **默认生成**：
   - 根据规则摘要，提炼 P2 的 3-5 步教学内容，生成教学页
   - 设计 P5 的 2-4 个进阶技巧，生成技巧页

3. **可选生成**（如用户明确指定）：
   - 提炼 P3 的 1-2 个核心刺激点，生成解析页
   - 确定 P4 场景类型，生成场景页

4. 逐页生成图片，保存到游戏目录
5. 展示生成的内页预览，确认风格一致性

> **输出说明**：默认输出规则图 + 2 张内页（P2 教学页 + P5 技巧页），如需 P3、P4 请在任务中明确说明。

## 子技能集成

本技能内置调用 `/boardgame-rule-graphic`，执行时自动生成规则讲解图，无需单独调用。
