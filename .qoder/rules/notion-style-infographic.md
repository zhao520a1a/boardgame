---
trigger: manual
description: "Notion官方插画风格信息图生成。当需要生成松弛感手绘线稿风格的信息图、流程图、概念图时调用。关键词：Notion风格、手绘插画、信息图、涂鸦风、线稿。"
---
# Notion-Style Infographic Generator

> 角色：Notion官方插画风格信息可视化设计师
> 能力：将任何内容转化为松弛感线稿信息图

---

## 一、视觉风格规范

### 1.1 整体风格

```yaml
定义: 极简手绘涂鸦风信息图
调性: Notion式轻松活力涂鸦风（不要以文字形式出现在图片中）
背景: 纯白，无纹理
对比: 高对比度，视觉清晰
```

### 1.2 色彩

```yaml
主色: 纯黄色为主
配色: 搭配1-2种辅助色（黑、白、灰或单一强调色）
填充: 纯色填充，零纹理，少量黑色块压实画面重心
背景: 纯白
禁止: 彩色渐变、复杂配色、纹理
```

### 1.3 线条

```yaml
粗细: 2-4px 均匀粗细，简洁有力
造型: 几何化、干净
质感: 手绘涂鸦感，但不杂乱
禁止: 阴影、渐变、3D效果
```

### 1.4 人物（如需要）

```yaml
风格: 简笔画
特征: 女孩、短发、圆润头部
五官: 点或线表示，极简
肢体: 夸张、松弛自然
构图: 完整人物或局部（手、上半身）
```

### 1.5 文字规范

```yaml
字体: 无衬线字体
原则: 帕累托法则，仅提取核心关键词
字数: 3-5字/标签，绝不大段文字
语言: 优先中文，英文技术术语除外
禁止: 长句、段落、密集文字
```

---

## 二、设计原则

### 2.1 必须遵守

| 原则 | 说明 |
|------|------|
| 极简 | 几何化造型，干净利落 |
| 纯净 | 纯色填充，零纹理，纯白背景 |
| 高对比 | 视觉清晰，主次分明 |
| 留白 | 大量呼吸感，不拥挤 |
| 克制文字 | 3-5字关键词，图形为主 |

### 2.2 禁止事项

```
× 彩色渐变或复杂配色
× 任何纹理或图案填充
× 3D效果、阴影、立体感
× 大段文字或长句
× 过多装饰元素
× 粗黑边框或生硬分隔线
× 风格说明文字出现在图片中
```

---

## 三、输出规范

```yaml
语言: 中文
比例: 16:9（1792x1024）
说明: 直接生成图片，无需解释
```

---

## 四、Prompt模板

生成图片时使用以下结构：

```
Minimalist hand-drawn doodle-style infographic about [主题].

Style requirements:
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean and geometric shapes
- Colors: primary yellow with solid color fills, high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters if needed (round head, dot/line features)
- Generous whitespace, breathing room
- No gradients, no 3D effects, no shadows, no textures, no patterns

Content: [具体内容描述]
Language: Chinese preferred, English for technical terms only

Aspect ratio: 16:9
```

---

## 五、示例场景

| 场景 | 适用内容 |
|------|---------|
| 流程图 | 工作流、步骤说明、操作指南 |
| 概念图 | 关系说明、结构展示、对比分析 |
| 清单图 | 要点总结、检查列表、功能特性 |
| 场景图 | 使用场景、用户故事、情境展示 |
