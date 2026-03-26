# 截码战 P4-场景页 配图 Prompt

> 目标：为《截码战》小红书笔记生成P4场景页 —「截码战最佳场景指南」
> 风格统一：A线文艺调性（暖棕手绘信息图）

---

## Prompt（英文版，适用于 Gemini 3 Image Pro）

```
A warm, hand-drawn style infographic showing the best social scenarios for playing the board game "Decrypto".

Style: Minimalist hand-drawn doodle-style infographic with warm literary tone.
- Warm cream/parchment background (#FFF8E7), subtle paper texture
- Line: 2-3px hand-drawn strokes in dark brown (#3E2723)
- Colors: warm red (#C41E3A), navy blue (#1B2A4A), honey gold (#DAA520), sage green (#6B8E6B)
- Doodle aesthetic: cozy, lifestyle, like a travel/lifestyle journal page
- Text: Chinese sans-serif font, 3-5 character keywords per label
- Simple stick-figure characters in various social settings

Content structure: Vertical checklist with 4 scenario cards.

Title at top: "什么时候玩截码战？" (large, bold, dark brown)
Subtitle: "这四个场景绝配" (smaller, honey gold)

Scenario 1 — "🎉 周末聚会" (Weekend Gathering):
- Rounded card with warm red left border
- Doodle: 4-6 stick figures around a table, drinks and snacks nearby
- Stats badge: "4-6人 | 30分钟 | 笑到停不下来"
- Star rating: ★★★★★

Scenario 2 — "🏢 团建破冰" (Team Building):
- Rounded card with navy blue left border
- Doodle: office-style stick figures loosening ties, getting competitive
- Stats badge: "6-8人 | 快速破冰 | 不尬聊"
- Star rating: ★★★★☆

Scenario 3 — "🎓 情侣/闺蜜局" (Couples/BFF Game Night):
- Rounded card with honey gold left border
- Doodle: 4 stick figures (2 couples or friend groups) in cozy setting with fairy lights
- Stats badge: "4人 | 默契考验 | 甜蜜博弈"
- Star rating: ★★★★★

Scenario 4 — "🧠 脑力训练营" (Brain Training):
- Rounded card with sage green left border
- Doodle: stick figures with gears/lightbulbs above heads, intense thinking poses
- Stats badge: "4-6人 | 逻辑思维 | 越玩越聪明"
- Star rating: ★★★★☆

Bottom note in hand-drawn speech bubble: "不适合：2-3人（人太少） | 沉默型聚会（需要互动）"

Aspect ratio: 3:4 (768x1024 pixels)
Layout: vertical, 4 scenario cards stacked with comfortable spacing
No watermarks, no UI elements
```

---

## 设计说明

### Organism Level（基础场景）
- **主题**：截码战最佳游玩场景推荐
- **核心传达**：帮读者快速判断"我适合玩这个游戏吗"，降低决策成本
- **调性**：轻松、生活化、场景代入感

### Molecule Level（细节细化）
- **关键信息元素**：4个场景（周末聚会、团建、情侣闺蜜、脑力训练）+ 排除场景
- **信息层级**：标题 → 4场景卡片（等权） → 底部排除提示
- **图表类型**：列表图（checklist）
- **图形元素**：场景卡片、简笔画人物、星级评分、标签

### Atomic Level（精细细节）
- **色彩编码**：红=聚会活力，蓝=团建专业，金=亲密甜蜜，绿=理性脑力
- **标签文字**：周末聚会、团建破冰、情侣闺蜜局、脑力训练营
- **布局**：纵向4张卡片堆叠
- **字体**：中文无衬线

### Parameters Level（技术参数）
- **图像比例**：3:4（768x1024）
- **色彩方案**：暖米底 + 四色左边框卡片
- **渲染风格**：暖色手绘信息图
- **输出格式**：小红书内页图
