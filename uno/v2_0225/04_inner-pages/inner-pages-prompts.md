# UNO 内页设计 - 图像生成提示词

## 设计概述

| 项目 | 规格 |
|------|------|
| 游戏名称 | UNO / 优诺 |
| 图片尺寸 | 768 x 1024 px (3:4) |
| 页数 | 4张（P2-P5） |
| 风格线 | B线（高点击率）- 与封面统一 |
| 配色方案 | UNO四色（红/黄/蓝/绿）+ 深色背景 |

---

## P2：教学页 - 「3步学会UNO」

### 内容设计
```
🎯 3步学会UNO

① 发牌准备
   每人7张手牌，翻开1张作为起始牌

② 轮流出牌
   打出颜色/数字/符号相同的牌
   没牌出？摸一张！

③ 喊"UNO"获胜
   手牌剩1张必须喊UNO
   第一个出完所有牌的人赢！
```

### Midjourney Prompt
```
A clean infographic teaching card for card game "UNO".
Dark background with UNO colors (red, yellow, blue, green) as accents.
3 numbered steps with large icons in card-style layout:
Step 1: Deal cards icon - "发牌准备"
Step 2: Play card icon - "轮流出牌"  
Step 3: Winner trophy icon - "喊UNO获胜"
Modern flat design, high contrast, easy to read at a glance.
Bold sans-serif typography, step-by-step tutorial format.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, educational infographic, party game energy.

--ar 3:4 --v 6
```

### Stable Diffusion Prompt
```
(infographic:1.3), tutorial card, UNO card game,
dark background, (neon accents:1.2), red yellow blue green,
3 numbered steps, icon-driven design,
modern flat style, (high readability:1.3),
Chinese text, bold typography,
educational layout, step by step,
768x1024, portrait,
<lora:infographic_style:0.7>

Negative: cluttered, blurry text, low contrast, English text
```

---

## P3：解析页 - 「UNO 为什么这么上瘾？」

### 内容设计
```
🔥 为什么UNO让人上瘾？

【刺激点1：+4制裁的快感】
📊 平均每局出现 3-5 次 +4
😈 被制裁：愤怒值 +100
😎 制裁别人：爽感值 MAX

【刺激点2：UNO喊牌的紧张感】
⏰ 剩1张牌 → 手心出汗
🎤 喊UNO → 全场焦点
😱 忘记喊 → 社死现场

【核心公式】
简单规则 × 功能牌互坑 × 社交欢乐 = 停不下来！
```

### Midjourney Prompt
```
An engaging analytical graphic for card game "UNO".
Dark background with vibrant UNO color accents.
Title: "为什么UNO让人上瘾" in bold Chinese text.
Two excitement zones visualized:
Zone 1: "+4 Card" - showing emotion meter from rage to satisfaction
Zone 2: "UNO Call" - showing tension buildup timeline
Dynamic comic-style layout with versus comparisons.
Meme-worthy expressions and reactions. Data visualization elements.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, infographic meets meme style.

--ar 3:4 --v 6
```

---

## P4：场景页 - 「聚会必备神器」

### 内容设计
```
📸 真实聚会场景

画面元素：
- 4-5个朋友围坐客厅沙发
- 有人刚打出+4，表情得意
- 有人被制裁，捂脸哀嚎
- 桌上散落着UNO卡牌
- 零食饮料点缀
- 暖色氛围灯光

氛围关键词：
欢笑 | 夸张反应 | 真实互动 | 派对能量
```

### Midjourney Prompt
```
A lifestyle photograph of young friends playing "UNO" at a party.
Cozy living room setting, fairy lights and warm ambient lighting.
Group of 4-5 people around a coffee table, UNO cards scattered.
One person triumphantly holding up a +4 Wild card with smug expression.
Another person dramatically covering their face in defeat.
Others laughing and pointing. Snacks and drinks visible.
Natural candid moment, genuine reactions, party game energy.
Cinematic warm color grading, authentic social atmosphere.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, lifestyle photography, viral party content.

--ar 3:4 --v 6
```

---

## P5：技巧页 - 「老玩家的4个秘密技巧」

### 内容设计
```
🎯 老玩家偷偷在用的4个技巧

① 记牌大法
   记住已出的+4和+2
   知道谁手里有"核弹"

② +4质疑时机
   对方刚出过同色牌？
   大胆质疑，反杀！

③ 万能牌留到最后
   别急着出万能牌
   关键时刻当救命稻草

④ 故意不喊UNO
   引诱对手提醒你
   然后说"我已经喊过了"（坏笑）

💬 你还有什么野路子？评论区分享！
```

### Midjourney Prompt
```
A tips and tricks card for card game "UNO".
Dark background with UNO color accents (red, yellow, blue, green).
Title: "老玩家的4个秘密技巧" in bold Chinese text.
4 pro tips in numbered card format with icons:
Tip 1: Memory icon - card counting strategy
Tip 2: Challenge icon - +4 bluff detection
Tip 3: Save icon - wild card timing
Tip 4: Sneaky face icon - UNO call tricks
Premium card design feel, collectible reference aesthetic.
Call-to-action at bottom. Gaming strategy guide style.
IMPORTANT: All text in the image must be in Chinese characters (汉字), clearly legible. Do NOT include any English text.
768x1024 portrait, strategy guide design, meme energy.

--ar 3:4 --v 6
```

---

## 设计一致性检查

| 检查项 | 要求 | 状态 |
|--------|------|------|
| 配色统一 | 深色背景 + UNO四色 | ✅ |
| 字体风格 | 粗体无衬线，高对比 | ✅ |
| 图标风格 | 扁平/填充，统一调性 | ✅ |
| 留白比例 | >= 20% | ✅ |
| 信息密度 | 每页聚焦单一主题 | ✅ |
| 文字语言 | 纯中文 | ✅ |

---

## 5P 完整结构预览

| 页码 | 类型 | 主题 | 核心目的 |
|------|------|------|---------|
| P1 | 封面 | 聚会不玩UNO等于白来 | 吸引点击 |
| P2 | 教学页 | 3步学会UNO | 降低门槛 |
| P3 | 解析页 | 为什么这么上瘾 | 激发兴趣 |
| P4 | 场景页 | 聚会真实画面 | 场景代入 |
| P5 | 技巧页 | 老玩家的秘密技巧 | 驱动收藏 |

---

*内页提示词生成完成 - v2_0225*
