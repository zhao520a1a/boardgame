# 情书 — 回合流程配图 Prompt

> 目标：为桌游《情书》的回合流程章节生成一张 Notion 风格手绘涂鸦信息图

---

## Prompt（中文版，适用于 Gemini 3 Image Pro）

```
Minimalist hand-drawn doodle-style infographic illustrating the turn flow of the card game "Love Letter".

Style requirements:
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean and geometric shapes
- Colors: primary yellow with solid color fills, 1-2 accent colors (black for outlines and text, light gray for secondary elements), high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show any style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters (round head, dot/line facial features, exaggerated relaxed limbs) to represent a player taking their turn
- Generous whitespace, breathing room between each step
- No gradients, no 3D effects, no shadows, no textures, no patterns

Content:
A clear top-to-bottom vertical flow chart with exactly 3 large numbered steps connected by playful hand-drawn arrows:

Step ①「抽牌」: A stick-figure character cheerfully drawing one card from a face-down deck. A small yellow speech bubble shows "手牌 → 2张". The deck is drawn as a simple rounded rectangle stack.

Step ②「出牌」: The same character placing one card face-up in front of themselves. The played card is highlighted with a yellow fill. A small label says "面朝上".

Step ③「执行能力」: A bold yellow starburst icon with a lightning bolt inside, representing the card's special ability being activated. A small label says "按牌执行".

Below the 3 steps, a thin dashed horizontal line separates a footer zone with two small icon-label pairs:
- A crossed-out stick figure with label "出局跳过"
- A circular clockwise arrow icon with label "顺时针轮流"

The overall layout reads like a simple one-page cheat sheet: vertical, top-aligned, with the title "回合流程" at the top in bold black sans-serif Chinese text. Each step is visually distinct and immediately understandable at a glance.

Language: Chinese preferred, English for technical terms only

Aspect ratio: 16:9
```

---

## 设计说明

### Organism Level（基础场景）
- **主题**：桌游《情书》的单回合操作流程
- **核心传达**：每回合只做三件事——抽牌、出牌、执行能力
- **调性**：轻松、清晰、新手友好

### Molecule Level（细节细化）
- **关键信息元素**：3个核心步骤 + 2个补充规则
- **信息层级**：标题 → 三步流程（主体） → 补充规则（次要）
- **图表类型**：纵向流程图（箭头连接）
- **图形元素**：简笔画人物、卡牌图标、牌堆、闪电星爆、顺时针箭头

### Atomic Level（精细细节）
- **色彩编码**：黄色=重点高亮/激活状态，黑色=轮廓与文字，灰色=次要信息
- **标签文字**：「抽牌」「出牌」「执行能力」「出局跳过」「顺时针轮流」
- **布局**：顶部标题 → 中部三步纵向排列 → 底部虚线分隔的补充区
- **字体**：无衬线，标题加粗，标签常规

### Parameters Level（技术参数）
- **图像比例**：16:9（1792×1024）
- **色彩方案**：纯黄色为主，黑白灰为辅
- **渲染风格**：Notion 式极简手绘涂鸦
- **输出格式**：信息图/流程图
