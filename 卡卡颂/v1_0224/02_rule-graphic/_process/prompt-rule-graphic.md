# 卡卡颂 — 规则速查图 Prompt

> 目标：为《卡卡颂》生成一张 Notion 手绘涂鸦风格 规则速查信息图

---

## Prompt（英文版，适用于 ImageGen）

```
A clean, visually organized board game rule reference card infographic for "Carcassonne" (卡卡颂).

Style: Minimalist hand-drawn doodle-style infographic, Notion-style relaxed and energetic aesthetic.
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean geometric shapes with hand-drawn doodle feel
- Colors: warm orange (#FF8C42) as primary accent, black outlines, white background, light orange tint (#FFF3E0) for section backgrounds
- Small amount of green (#7CB342) for grass/field elements and blue (#42A5F5) for road elements as secondary accents
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Generous whitespace, breathing room between sections
- No gradients, no 3D effects, no shadows, no complex textures

Layout (768x1024 portrait, top to bottom):

TOP BANNER (8%):
- Title: "卡卡颂 Carcassonne" in bold
- Right side small badges: "2~5人" "35min" "7+"
- Subtitle line: "拼地图 · 放小人 · 抢地盘"

GOAL BAR (7%):
- Orange-tinted rounded rectangle
- Trophy icon + "目标：72张拼图用完时 积分最高者获胜"

CORE FLOW SECTION (35%):
- Section header: "每回合三步" with circled numbers
- Vertical flow chart with 3 large rounded-rectangle steps connected by downward arrows:
  - Step 1: hand icon + "抽拼图" → "从牌堆抽1张翻开"
  - Step 2: puzzle piece icon + "放拼图" → "边必须匹配" with 3 small matching icons showing: road=road, city=city, grass=grass
  - Step 3: meeple figure icon + "放小人" → "(可选) 占领区域" with tag "每回合最多1个"
- Small note at bottom: arrow pointing right → "区域完成？立刻计分+收回小人"

FOUR ROLES SECTION (18%):
- Section header: "四种小人角色"
- 2x2 icon grid, each cell has a simple meeple figure in different pose:
  - Top-left: standing meeple on road line → "路霸" (道路)
  - Top-right: meeple with castle icon → "骑士" (城市)
  - Bottom-left: meeple with small house → "修士" (修道院)
  - Bottom-right: lying meeple on grass → "农民" (进阶)

SCORING TABLE (20%):
- Section header: "计分速查"
- Clean table/grid with orange header row:
  - Column headers: 区域 | 完成时 | 未完成
  - Row 1: road icon "道路" | "每张1分" | "每张1分"
  - Row 2: castle icon "城市" | "每张2分+盾牌2分" | "每张1分+盾牌1分"
  - Row 3: house icon "修道院" | "九宫格=9分" | "已拼几张算几分"
  - Row 4: lying meeple "农民" | "—" | "每完成城市3分"

WARNING SECTION (12%):
- Orange-bordered alert box with warning triangle icon
- Three short bullet points with X/check marks:
  - "⚠ 先放小人，再计分"
  - "⚠ 已占领区域不能直接放人"
  - "⚠ 每人仅7个小人，节奏是关键"

Overall: informational graphic design, high readability, clean doodle aesthetic, warm orange-white color scheme, portrait orientation 768x1024.
```

---

## 设计说明

### Organism Level（基础场景）
- **主题**：卡卡颂完整规则速查图
- **核心传达**：新手5分钟内理解回合流程、角色分工和计分规则
- **调性**：轻松友好、Notion手绘涂鸦风、橙白暖色调

### Molecule Level（细节细化）
- **关键信息元素**：游戏参数、获胜条件、3步回合流程、4种小人角色、计分表、注意事项
- **信息层级**：回合流程（核心50%）→ 计分规则（30%）→ 角色+警示（20%）
- **图表类型**：混合型（流程图+网格+表格+警示框）
- **图形元素**：meeple小人图标、拼图图标、城堡/道路/修道院图标、箭头流程线

### Atomic Level（精细细节）
- **色彩编码**：橙色=#FF8C42（主色/高亮）、浅橙=#FFF3E0（区块背景）、绿色=#7CB342（草地）、蓝色=#42A5F5（道路）
- **标签文字**：抽拼图、放拼图、放小人、路霸、骑士、修士、农民（均3字以内）
- **布局**：标题8%→目标7%→流程35%→角色18%→计分20%→警示12%
- **字体**：中文无衬线，标题加粗，标签常规

### Parameters Level（技术参数）
- **图像比例**：3:4（768x1024）
- **色彩方案**：橙白主色调 + 绿蓝辅色
- **渲染风格**：Notion 手绘涂鸦风（notion-doodle 变体）
- **输出格式**：PNG 信息图
