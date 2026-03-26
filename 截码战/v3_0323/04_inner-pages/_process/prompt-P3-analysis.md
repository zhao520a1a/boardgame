# 截码战 P3-解析页 配图 Prompt

> 目标：为《截码战》小红书笔记生成P3解析页 —「提示词的艺术：太直白vs太隐晦」
> 风格统一：A线文艺调性（暖棕手绘信息图）

---

## Prompt（英文版，适用于 Gemini 3 Image Pro）

```
A warm, hand-drawn style infographic explaining the art of writing clues in the board game "Decrypto" — comparing "too obvious" vs "too obscure" clue strategies.

Style: Minimalist hand-drawn doodle-style infographic with warm literary tone.
- Warm cream/parchment background (#FFF8E7), subtle paper texture
- Line: 2-3px hand-drawn strokes in dark brown (#3E2723), slightly uneven for organic feel
- Colors: warm red (#C41E3A) for "wrong/danger", sage green (#6B8E6B) for "correct/safe", navy (#1B2A4A) for neutral
- Doodle aesthetic: cozy, approachable, like explaining to a friend
- Text: Chinese sans-serif font, 3-5 character keywords per label
- Simple stick-figure characters with emotions (happy, worried, confused)

Content structure: Side-by-side comparison with a "sweet spot" conclusion.

Title at top: "提示词的艺术" (large, bold, dark brown)
Subtitle: "太直白被截 vs 太隐晦队友懵" (smaller, warm red)

Left column — "❌ 太直白" (Too Obvious):
- Header in red rounded box
- Example: Target word "奶牛" → Clue "牛奶" 
- Doodle: opposing team spy with magnifying glass, grinning (easy intercept)
- Result icon: red "截获!" stamp
- Stick figure of teammate looking worried

Right column — "❌ 太隐晦" (Too Obscure):
- Header in grey rounded box
- Example: Target word "奶牛" → Clue "宇宙"
- Doodle: teammate with "???" above head, completely confused
- Result icon: black "猜错!" stamp
- Stick figure scratching head

Bottom section — "✅ 刚刚好" (Just Right):
- Header in sage green rounded box, centered below both columns
- Example: Target word "奶牛" → Clue "铁桶" (milking needs a bucket)
- Doodle: teammate with lightbulb moment, spy with confused face
- Golden highlight border around this section
- Label: "队友秒懂，对手懵圈"

Visual divider: hand-drawn vertical dashed line between left and right columns

Aspect ratio: 3:4 (768x1024 pixels)
Layout: vertical, two columns in upper 60%, centered conclusion in lower 30%, title in top 10%
No watermarks, no UI elements
```

---

## 设计说明

### Organism Level（基础场景）
- **主题**：截码战核心机制解析——提示词的艺术
- **核心传达**：好提示词 = "队友能猜对 + 对手猜不到" 的平衡点
- **调性**：趣味、启发、让人想试试

### Molecule Level（细节细化）
- **关键信息元素**：太直白（被截获）、太隐晦（队友猜错）、刚刚好（完美平衡）
- **信息层级**：标题 → 正反对比（等权） → 正确答案（重点强调）
- **图表类型**：对比图（comparison）
- **图形元素**：对比分栏、表情人物、示例词语、✓/✗图标

### Atomic Level（精细细节）
- **色彩编码**：红色=危险/错误，绿色=正确，灰色=次要错误
- **标签文字**：太直白、太隐晦、刚刚好、队友秒懂对手懵圈
- **布局**：上部双栏对比，下部居中结论
- **字体**：中文无衬线

### Parameters Level（技术参数）
- **图像比例**：3:4（768x1024）
- **色彩方案**：暖米底 + 红绿对比 + 金色高亮
- **渲染风格**：暖色手绘信息图
- **输出格式**：小红书内页图
