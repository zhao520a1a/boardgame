# 情书 (Love Letter) — 一轮结束 配图 Prompt

> 目标：为 情书规则 的 ROUND_END（一轮怎么结束）章节生成一张 Notion 极简手绘涂鸦风 风格 流程图

---

## Prompt（英文版，适用于 Gemini 3 Image Pro）

```
Minimalist hand-drawn doodle-style infographic illustrating a vertical flow chart about Love Letter Round End Conditions.

Style: Minimalist hand-drawn doodle-style infographic.
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean geometric shapes
- Colors: primary yellow (#FFD93D) with solid fills, high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters if needed (round head, dot/line features, exaggerated relaxed limbs)
- Generous whitespace, breathing room
- No gradients, no 3D effects, no shadows, no textures, no patterns

Content structure: Vertical flow chart with decision branches.
- Top title: "一轮结束" in bold
- Decision diamond 1: "只剩一人?" with stick figure icon
  - Yes branch (right arrow): "直接获胜!" with trophy doodle icon
- Decision diamond 2: "牌堆抽完?" with empty deck icon
  - Yes branch (right arrow): "亮牌比点数" with cards comparison icon
    - Sub-decision: "点数相同?"
      - Yes: "比出牌总和" → still tied? → "共同获胜" with handshake icon
      - No: "点数大者胜" with crown icon
- Bottom section in yellow rounded box: "赢家奖励"
  - "获得1枚爱心" with heart icon
  - "重新洗牌" with shuffle icon
  - "赢家先手开始新一轮" with play/start icon
- Decision diamonds use diamond shapes, outcomes use rounded rectangles
- Connecting arrows with clear Yes/No labels in Chinese ("是"/"否")

Content:
A round of Love Letter ends in two possible ways: (1) Only one player remains after all others are eliminated — that player wins immediately. (2) The deck runs out — all surviving players reveal hands and compare values, highest wins. Tiebreaker: compare total value of all played cards; if still tied, those players share the victory. The round winner receives one love token, then reshuffle and start a new round with the winner going first.

Language: Chinese preferred, English for technical terms only

Aspect ratio: 3:4 (768x1024 pixels)
Layout: vertical composition, top-to-bottom information flow
Title placement: top third area, bold and attention-grabbing
Key content: center zone (thumb zone for mobile viewing)
Bottom space: optional branding or supplementary info
```

---

## 设计说明

### Organism Level（基础场景）
- **主题**：情书桌游一轮结束条件与判定流程
- **核心传达**：两种结束方式（淘汰剩一人/牌堆抽完比点数），加上平局处理和赢家奖励
- **调性**：清晰逻辑、决策导向、新手友好

### Molecule Level（细节细化）
- **关键信息元素**：2个结束条件（只剩一人/牌堆抽完）、点数比较规则、平局处理（比出牌总和/共同获胜）、赢家奖励（爱心标记+重新开局）
- **信息层级**：结束条件判定为主体 → 平局处理为次要 → 赢家奖励为补充
- **图表类型**：纵向流程图 (flowchart) + 决策分支
- **图形元素**：菱形决策框、圆角矩形结果框、方向箭头（是/否标签）、小图标（奖杯/卡牌/爱心/握手）

### Atomic Level（精细细节）
- **色彩编码**：黄色(#FFD93D)=决策框和奖励区填充色、黑色=轮廓和文字、白色=背景
- **标签文字**：「一轮结束」「只剩一人?」「直接获胜!」「牌堆抽完?」「亮牌比点数」「点数相同?」「比出牌总和」「共同获胜」「点数大者胜」「赢家奖励」「获得1枚爱心」「重新洗牌」「赢家先手」
- **布局**：顶部标题 → 中部决策流程纵向排列（两个菱形判定 + 分支结果）→ 底部赢家奖励区
- **字体**：标题加粗无衬线、判定问题加粗、结果标签常规无衬线

### Parameters Level（技术参数）
- **图像比例**：3:4（768x1024 pixels）
- **色彩方案**：主色 #FFD93D（黄色），辅色 黑色轮廓 + 白色背景
- **渲染风格**：Notion 极简手绘涂鸦风 (notion-doodle)
- **输出格式**：社交媒体竖版信息图
