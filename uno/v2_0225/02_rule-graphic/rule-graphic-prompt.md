# UNO 规则速查图 - 图像生成提示词

## 设计概述

| 项目 | 规格 |
|------|------|
| 游戏名称 | UNO / 优诺 |
| 图片尺寸 | 768 x 1024 px (3:4) |
| 风格线 | B线（高点击率）- 活泼明快 |
| 配色方案 | UNO经典四色（红/黄/蓝/绿）+ 深色背景 |
| 信息密度 | 65% 功能 + 35% 风格 |

---

## 内容结构

### 区域 1：标题区（顶部 10%）
```
UNO 规则速查
3分钟学会聚会神器
```

### 区域 2：主题 & 获胜条件（15%）
```
🎯 目标：第一个出完手牌的人获胜
💡 核心：颜色/数字/符号 三选一匹配出牌
```

### 区域 3：游戏准备（10%）
```
📦 准备阶段
• 每人发 7 张手牌
• 翻开 1 张作为起始牌
• 发牌员左边玩家开始
```

### 区域 4：回合流程（30%）- 流程图
```
┌──────┐    ┌──────┐    ┌──────┐
│ 出牌  │ →  │ 摸牌  │ →  │ 效果  │
│      │    │(没牌时)│    │(功能牌)│
└──────┘    └──────┘    └──────┘

出牌条件：
✓ 颜色相同
✓ 数字相同  
✓ 符号相同
✓ 万能牌（随时出）
```

### 区域 5：卡牌效果（25%）- 图标网格
```
┌─────────────────────────────────┐
│  ↩️ 转向牌    │  改变出牌方向     │
│  🚫 禁止牌    │  跳过下家        │
│  +2 牌      │  下家摸2张       │
│  🌈 万能牌   │  指定任意颜色     │
│  +4 万能牌  │  下家摸4张+指定色  │
└─────────────────────────────────┘
```

### 区域 6：特殊规则警示（10%）
```
⚠️ 记住这些！
• 手牌剩1张必须喊 "UNO"，否则罚摸2张
• +4 必须手里没有同色牌才能打，可被质疑
• 双人局：转向牌 = 跳过牌
```

---

## Midjourney Prompt

```
A vibrant, clear board game rule reference infographic for "UNO".

Layout: vertical 3:4 portrait format, dark background with bright UNO card colors (red, yellow, blue, green) as accent colors.

Content sections from top to bottom:
1. Title banner "UNO Rules" with game logo style
2. Goal section with target icon
3. Setup checklist with card icons
4. Turn flow diagram with arrows showing: Play Card → Draw Card → Apply Effect
5. Card effect grid showing: Reverse, Skip, +2, Wild, +4 Wild with icons
6. Warning box for special rules (UNO call, +4 challenge)

Style: modern infographic design, clean typography, high contrast, party game energy, informational yet playful.

Colors: vibrant red #FF5555, yellow #FFDD00, blue #5555FF, green #55AA55 on dark gray #1A1A1A background.

Text: Chinese characters, clear hierarchy, minimum 12pt equivalent.

Mood: energetic, fun, easy to read at a glance, suitable for social media sharing.

--ar 3:4 --v 6
```

## 设计要点提醒

1. **层级清晰**：标题 > 区块标题 > 正文，用字号和颜色区分
2. **图标优先**：功能牌效果用图标+短文字，避免长段落
3. **流程可视化**：回合流程用箭头流程图，不用纯文字列表
4. **警示突出**：特殊规则用橙色/红色边框框出
5. **留白适度**：信息密集区域保持 20% 以上留白

---

*规则图提示词生成完成 - v2_0225*
