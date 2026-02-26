# 情书 (Love Letter) — 卡牌效果 配图 Prompt

> 目标：为 情书规则 的 CARDS（卡牌效果）章节生成一张 Notion 极简手绘涂鸦风 风格 列表图

---

## Prompt（英文版，适用于 Gemini 3 Image Pro）

```
Minimalist hand-drawn doodle-style infographic illustrating a visual checklist about Love Letter Card Abilities Reference.

Style: Minimalist hand-drawn doodle-style infographic.
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean geometric shapes
- Colors: primary yellow (#FFD93D) with solid fills, high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters if needed (round head, dot/line features, exaggerated relaxed limbs)
- Generous whitespace, breathing room
- No gradients, no 3D effects, no shadows, no textures, no patterns

Content structure: Vertical checklist with 8 items in clean arrangement.
- Title at top: "卡牌速查" in bold
- 8 card entries, each row showing: number badge in yellow circle + role name bold + card count + one-line ability icon
- Item 1: "1 卫兵 ×5" — magnifying glass icon — "猜牌淘汰"
- Item 2: "2 神父 ×2" — eye icon — "偷看手牌"
- Item 3: "3 男爵 ×2" — crossed swords icon — "比点出局"
- Item 4: "4 侍女 ×2" — shield icon — "护盾一轮"
- Item 5: "5 王子 ×2" — refresh/cycle icon — "弃牌重抽"
- Item 6: "6 国王 ×1" — swap arrows icon — "交换手牌"
- Item 7: "7 伯爵夫人 ×1" — exclamation icon — "必须先出"
- Item 8: "8 公主 ×1" — skull/danger icon — "出即出局"
- Each item uses consistent layout: left number badge in yellow circle, role name bold, ability keyword on right
- Clear visual separation between items with generous spacing
- Optional: subtle danger indicator on Princess (item 8) to highlight the risk

Content:
Love Letter has 16 cards with 8 unique roles numbered 1-8. Higher numbers are rarer but not necessarily stronger. Guard (×5) guesses to eliminate, Priest (×2) peeks at hands, Baron (×2) compares values, Handmaid (×2) grants immunity, Prince (×2) forces discard, King (×1) swaps hands, Countess (×1) must be played when paired with King or Prince, Princess (×1) causes instant elimination if played for any reason.

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
- **主题**：情书桌游卡牌效果速查表
- **核心传达**：8种角色牌各有独特能力，点数越高越稀有但不一定越强
- **调性**：清晰实用、一目了然、新手速查

### Molecule Level（细节细化）
- **关键信息元素**：8种角色（点数1-8），每种包含：点数、角色名、张数、能力关键词
- **信息层级**：角色列表为主体 → 各角色能力为次要细节
- **图表类型**：纵向列表图 (checklist)
- **图形元素**：黄色圆形数字徽章、角色名文字、能力图标（放大镜/眼睛/剑/盾/循环/交换箭头/感叹号/骷髅）

### Atomic Level（精细细节）
- **色彩编码**：黄色(#FFD93D)=数字徽章底色、黑色=轮廓和文字、白色=背景、可选红色标记公主危险性
- **标签文字**：「卡牌速查」「卫兵」「神父」「男爵」「侍女」「王子」「国王」「伯爵夫人」「公主」「猜牌淘汰」「偷看手牌」「比点出局」「护盾一轮」「弃牌重抽」「交换手牌」「必须先出」「出即出局」
- **布局**：顶部标题区 → 中部8行角色列表纵向排列（每行：圆形数字+角色名+张数+能力图标+能力关键词）→ 底部留白
- **字体**：标题加粗无衬线、角色名加粗、能力关键词常规无衬线

### Parameters Level（技术参数）
- **图像比例**：3:4（768x1024 pixels）
- **色彩方案**：主色 #FFD93D（黄色），辅色 黑色轮廓 + 白色背景
- **渲染风格**：Notion 极简手绘涂鸦风 (notion-doodle)
- **输出格式**：社交媒体竖版信息图
