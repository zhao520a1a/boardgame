# 情书 (Love Letter) — 回合流程 配图 Prompt

> 目标：为 情书规则 的 TURN_FLOW（回合流程）章节生成一张 Notion 极简手绘涂鸦风 风格 流程图

---

## Prompt（英文版，适用于 Gemini 3 Image Pro）

```
Minimalist hand-drawn doodle-style infographic illustrating a vertical flow chart about Love Letter Board Game Turn Flow.

Style: Minimalist hand-drawn doodle-style infographic.
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean geometric shapes
- Colors: primary yellow (#FFD93D) with solid fills, high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters if needed (round head, dot/line features, exaggerated relaxed limbs)
- Generous whitespace, breathing room
- No gradients, no 3D effects, no shadows, no textures, no patterns

Content structure: Vertical flow chart with 3 main steps.
- Start point clearly marked at top: "你的回合"
- Step 1 in rounded rectangle: "抽一张牌" with small card icon, description: draw one card from deck (now holding 2 cards)
- Step 2 in rounded rectangle: "打出一张" with face-up card icon, description: play one card face-up in front of you
- Step 3 in rounded rectangle: "执行能力" with lightning bolt icon, description: activate the played card's ability immediately
- Connecting arrows with clear downward direction between steps
- End point: "下一位玩家" with clockwise arrow icon
- Bottom section: two supplementary rules with small icons:
  - "出局者亮手牌" with eye icon
  - "出牌保留可见" with cards icon

Content:
Each player's turn consists of exactly 3 simple actions: Draw one card from the deck (now holding 2), play one card face-up, and immediately execute its ability. Then it's the next player's turn clockwise. Eliminated players skip their turns and must reveal their hand. All played cards remain face-up for information tracking.

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
- **主题**：情书桌游回合流程教学图
- **核心传达**：每个人的回合只做三件事——抽牌、出牌、执行能力，简单易学
- **调性**：轻松新手友好、松弛感、鼓励尝试

### Molecule Level（细节细化）
- **关键信息元素**：3个主要步骤（抽牌/出牌/执行能力）+ 2条补充规则（出局亮牌/出牌保留可见）+ 起终点标记
- **信息层级**：3步流程为主体 → 补充规则为次要
- **图表类型**：纵向流程图 (flowchart)
- **图形元素**：圆角矩形步骤框、方向箭头、小图标（卡牌/闪电/眼睛/顺时针箭头）、可选简笔人物

### Atomic Level（精细细节）
- **色彩编码**：黄色(#FFD93D)=步骤框填充色、黑色=轮廓和文字、白色=背景
- **标签文字**：「你的回合」「抽一张牌」「打出一张」「执行能力」「下一位玩家」「出局者亮手牌」「出牌保留可见」
- **布局**：顶部标题区（"你的回合"起点）→ 中部三步流程纵向排列 → 底部补充规则区
- **字体**：标题加粗无衬线、步骤标签常规无衬线、补充说明小号

### Parameters Level（技术参数）
- **图像比例**：3:4（768x1024 pixels）
- **色彩方案**：主色 #FFD93D（黄色），辅色 黑色轮廓 + 白色背景
- **渲染风格**：Notion 极简手绘涂鸦风 (notion-doodle)
- **输出格式**：社交媒体竖版信息图
