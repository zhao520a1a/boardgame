---
trigger: manual
description: "通用文章配图提示词生成。支持多风格（Notion/科技感/水彩/线稿）、多图表类型（流程图/对比图/时间轴等）、多输出场景（文章/社媒/幻灯片），基于 Atomic Prompting 方法论自动生成适用于 Gemini 3 Image Pro 的英文 Prompt 及中文设计说明。关键词：配图生成、Prompt、信息图、风格预设、Atomic Prompting。"
---

# 文章配图提示词生成规则

> 角色：通用信息可视化设计 Prompt 工程师
> 能力：根据文档内容和参数配置，自动生成高质量的图像生成 Prompt
> 输出：适用于 Gemini 3 Image Pro 的完整 Prompt 文件（英文 Prompt + 中文四层 Atomic 设计说明）

---

## 一、参数定义

### 1.1 必填参数

| 参数名 | 类型 | 说明 | 示例 |
|-------|------|------|------|
| `DOCUMENT_FILE_PATH` | string | 源文档的完整路径 | `./docs/gameplay-guide.md` |

### 1.2 可选参数（含默认值）

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|--------|------|
| `chapter` | string | 要配图的章节名称,默认所有 | `回合流程` |
| `i` | integer | 输出序号（用于文件命名） | `1` |
| `style_preset` | enum | `notion-doodle` | 风格预设标识符，见§2.1 |
| `chart_type` | enum | `auto` | 图表类型，见§3，`auto` 为自动识别 |
| `output_scene` | enum | `article-16-9` | 输出场景，见§4.1 |
| `language` | enum | `zh-CN` | 图片中文字的主要语言 |
| `primary_color` | string | 继承风格预设 | 主色覆盖（HEX 或色彩名） |
| `extract_mode` | enum | `auto` | 内容提取模式：`auto` / `manual` / `full-chapter` |
| `custom_instructions` | string | `null` | 额外的自定义设计指令 |

### 1.3 参数验证规则

执行生成前必须验证：

```yaml
必填参数:
  - DOCUMENT_FILE_PATH 必须存在且可读
  - chapter 必须非空字符串
  - i 必须为正整数

可选参数:
  - style_preset 必须在注册表§2.1中存在
  - chart_type 必须在注册表§3中存在或为 auto
  - output_scene 必须在注册表§4.1中存在
  - language 必须为 ISO 639-1 语言代码
```

**验证失败处理**：中断执行，返回明确错误信息，指引用户修正参数。

---

## 二、风格预设注册表

### 2.1 风格索引表

| 预设标识符 | 风格名称 | 适用场景 | 参考规则 |
|-----------|---------|---------|---------|
| `notion-doodle` | Notion 极简手绘涂鸦风 | 教程、流程、概念图 | `notion-style-infographic.md` |
| `tech-info` | 科技感信息图风 | 数据可视化、技术文档 | §2.3 |
| `watercolor-hand` | 水彩手绘风 | 人文、生活、情感类内容 | §2.4 |
| `minimal-line` | 极简线稿风 | 专业报告、学术文章 | §2.5 |

---

### 2.2 Notion 极简手绘涂鸦风 (`notion-doodle`)

**定位**：松弛感、亲和力、新手友好，适合教程和流程说明。

**完整规范**：参见 `notion-style-infographic.md`

**快速参数摘要**：

```yaml
背景: 纯白（#FFFFFF），零纹理
主色: 纯黄色（#FFD93D）
辅色: 黑色轮廓，1-2种强调色（灰色、白色）
线条: 2-4px 均匀粗细，几何化、手绘涂鸦感
文字: 无衬线字体，3-5字关键词，中文优先
人物: 简笔画，圆润头部，点线五官，夸张松弛肢体
禁止:
  - 彩色渐变或复杂配色
  - 任何纹理或图案填充
  - 3D效果、阴影、立体感
  - 大段文字或长句
  - 风格说明文字出现在图中
```

**Prompt 插槽片段**：

```
Style: Minimalist hand-drawn doodle-style infographic.
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean geometric shapes
- Colors: primary yellow (#FFD93D) with solid fills, high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters if needed (round head, dot/line features, exaggerated relaxed limbs)
- Generous whitespace, breathing room
- No gradients, no 3D effects, no shadows, no textures, no patterns
```

---

### 2.3 科技感信息图风 (`tech-info`)

**定位**：现代、专业、数据驱动，适合技术文档和商业分析。

**视觉参数**：

```yaml
背景: 深色（#1A1A2E）或纯白，可选微弱网格
主色: 科技蓝（#0F4C81）、荧光青（#00D9FF）
辅色: 电路板绿、警示橙、深灰
线条: 1-2px 精细线条，几何锐利
装饰: 网格、数据点、进度条、图标化元素
字体: 等宽字体（代码感）或现代无衬线
特效: 渐变允许（科技感渐变）、发光效果
禁止:
  - 手绘涂鸦风格
  - 暖色调为主
  - 卡通元素
```

**Prompt 插槽片段**：

```
Style: Modern tech-inspired infographic design.
- Background: dark navy (#1A1A2E) or pure white with subtle grid pattern
- Colors: tech blue (#0F4C81) primary, neon cyan (#00D9FF) accent, circuit green highlights
- Lines: 1-2px sharp geometric lines, clean edges, precision aesthetic
- Elements: data points, progress bars, circuit board aesthetics, modern flat icons
- Text: monospace or modern sans-serif font, clear hierarchy, Chinese with English technical terms
- Effects: tech gradients allowed, subtle glow effects on key elements
- No hand-drawn elements, no warm tones, no cartoon characters
```

---

### 2.4 水彩手绘风 (`watercolor-hand`)

**定位**：温暖、人文、情感共鸣，适合生活类、情感类内容。

**视觉参数**：

```yaml
背景: 纸质纹理感白底或淡彩渲染
主色: 柔和暖色系（粉#FFB5BA、橙#FFD4A3、暖黄#FFF3B0、浅绿#B8E0D2）
辅色: 自然调和的邻近色，大地色系
线条: 不规则手绘线条，边缘柔和
装饰: 水彩晕染、手绘插画、自然元素（花叶、云朵）
字体: 手写风格或柔和无衬线
特效: 水彩晕染、颜色渗透、纸质纹理
禁止:
  - 生硬几何形状
  - 高饱和荧光色
  - 机械感/科技感元素
```

**Prompt 插槽片段**：

```
Style: Watercolor hand-painted illustration style.
- Background: light textured paper (white or cream) with subtle paper grain
- Colors: soft warm palette (blush pink #FFB5BA, warm orange #FFD4A3, pastel yellow #FFF3B0, sage green #B8E0D2)
- Lines: irregular hand-drawn strokes, soft edges with natural paint bleed
- Elements: watercolor splashes, hand-drawn illustrations, natural motifs (leaves, flowers, clouds)
- Text: handwritten-style or soft rounded sans-serif font, Chinese preferred
- Effects: watercolor wash textures, color blending, organic flow
- No sharp geometric shapes, no neon colors, no mechanical elements
```

---

### 2.5 极简线稿风 (`minimal-line`)

**定位**：克制、专业、学术，适合正式报告和专业出版物。

**视觉参数**：

```yaml
背景: 纯白（#FFFFFF）
主色: 纯黑（#000000）
辅色: 单一强调色（可选），灰阶
线条: 0.5-1px 精确线条，极简几何
装饰: 无装饰，仅必要图形元素
字体: 经典无衬线，字重明确
特效: 禁止一切特效
禁止:
  - 任何彩色（除单一强调色外）
  - 装饰性元素
  - 复杂图案
  - 阴影、渐变
```

**Prompt 插槽片段**：

```
Style: Minimalist black line art diagram.
- Background: pure white (#FFFFFF), absolutely clean, no texture
- Colors: black (#000000) primary, single accent color optional, grayscale for shading
- Lines: 0.5-1px precise geometric lines, minimal strokes, highly simplified
- Elements: essential shapes only, no decorative elements whatsoever
- Text: classic sans-serif font, clear weight hierarchy, Chinese preferred
- Effects: none, pure line art aesthetic
- Extreme simplicity, abstract representation, no colors beyond black/white/accent
```

---

### 2.6 风格扩展指南

新增风格时：

1. 在§2.1 索引表中添加一行（标识符、名称、适用场景、参考章节）
2. 在§2.x 中新增章节，采用以下结构：
   - **定位**：一句话说明适合什么场景
   - **视觉参数**：YAML 格式，包含背景/主色/辅色/线条/装饰/字体/特效/禁止
   - **Prompt 插槽片段**：可直接插入模板的英文描述
3. 无需修改其他章节，扩展完成

---

## 三、图表类型注册表

每种图表类型提供**识别关键词**（用于 `auto` 模式）和**Prompt 指引片段**。

---

### 3.1 流程图 (`flowchart`)

**识别关键词**：步骤、流程、顺序、操作、然后、接着、先、再、最后、阶段、环节

**内容结构提示**：
- 起点 → 步骤1 → 步骤2 → ... → 终点
- 每步一个动词短语 + 简洁说明
- 决策点用菱形，动作用矩形
- 箭头清晰标注流向

**Prompt 指引片段**：

```
Content structure: [Vertical/Horizontal] flow chart with [N] steps.
- Start point clearly marked
- Each step in [rounded rectangle / diamond for decisions]
- Connecting arrows with clear direction indicators
- Step labels: [Step 1 label], [Step 2 label], ...
- Optional: side annotations, loop-back indicators, decision branches
- Clean spacing between nodes for readability
```

---

### 3.2 对比图 (`comparison`)

**识别关键词**：对比、比较、vs、优点、缺点、区别、不同、选择、优劣、差异

**内容结构提示**：
- A vs B 左右分栏，或上下分区
- 对比维度清晰列出（3-5个维度）
- 视觉区分（颜色、图标、符号）
- 突出关键差异点

**Prompt 指引片段**：

```
Content structure: Side-by-side comparison layout.
- Left column: [Option A] with key points
- Right column: [Option B] with key points
- Comparison dimensions: [Dimension 1], [Dimension 2], [Dimension 3]
- Visual differentiation: contrasting colors, ✓/✗ icons for pros/cons
- Highlight key differences with accent color or bold markers
- Clear visual divider between columns
```

---

### 3.3 时间轴 (`timeline`)

**识别关键词**：时间线、历程、发展、演变、阶段、里程碑、进程、历史、迭代

**内容结构提示**：
- 横向或纵向时间线主轴
- 时间节点清晰标注
- 每个节点：时间标签 + 事件描述 + 图标/图示
- 可选：阶段分组、里程碑高亮

**Prompt 指引片段**：

```
Content structure: [Horizontal/Vertical] timeline diagram.
- Main timeline axis with clear direction (left→right or top→bottom)
- Time markers: [Date/Phase 1], [Date/Phase 2], [Date/Phase 3]
- Event nodes: icon + time label + brief description
- Optional: milestone highlights with larger nodes, phase groupings with background shading
- Consistent spacing between events
```

---

### 3.4 思维导图 (`mindmap`)

**识别关键词**：思维导图、脑图、关系、关联、分支、延伸、扩展、发散

**内容结构提示**：
- 中心主题节点
- 主分支（2-5个）从中心发散
- 次级分支细化
- 用颜色、线条粗细区分层级

**Prompt 指引片段**：

```
Content structure: Radial mind map with central node.
- Center: [Core theme] as main focal point
- Main branches (2-5): [Branch 1], [Branch 2], [Branch 3] radiating outward
- Sub-branches with detailed points extending from main branches
- Visual hierarchy: thicker lines for main branches, color coding per branch family
- Organic curved connecting lines, not rigid straight lines
```

---

### 3.5 树状图 (`tree`)

**识别关键词**：层级、分类、组织结构、从属关系、包含、隶属、上下级、分解

**内容结构提示**：
- 顶层根节点
- 树状分层结构（2-4层）
- 父子关系清晰
- 同级节点对齐

**Prompt 指引片段**：

```
Content structure: Hierarchical tree diagram.
- Root node at top: [Root label]
- Level 2 nodes: [Node 2.1], [Node 2.2] branching down
- Level 3 nodes: further subdivisions if needed
- Clear parent-child relationships with straight or angled connecting lines
- Aligned nodes at same hierarchy level
- Consistent vertical spacing between levels
```

---

### 3.6 矩阵图 (`matrix`)

**识别关键词**：矩阵、四象限、分类、定位、坐标、高低、重要、紧急、维度

**内容结构提示**：
- 横纵两轴定义维度
- 2x2 或 3x3 分区
- 每个象限：标签 + 内容元素
- 坐标轴标注清晰

**Prompt 指引片段**：

```
Content structure: 2x2 or 3x3 matrix diagram.
- Horizontal axis: [X-axis label] (low → high)
- Vertical axis: [Y-axis label] (low → high)
- Quadrants labeled: [Q1 name], [Q2 name], [Q3 name], [Q4 name]
- Items positioned in relevant quadrants with icons or text labels
- Clear axis labels at ends, optional gridlines for reference
```

---

### 3.7 列表图 (`checklist`)

**识别关键词**：清单、列表、要点、检查项、特点、功能、包含、具备、枚举

**内容结构提示**：
- 垂直排列的项目列表
- 每项：图标/序号 + 标题 + 简短说明
- 可选：复选框、优先级标记
- 视觉分隔清晰

**Prompt 指引片段**：

```
Content structure: Vertical checklist or list layout.
- [N] items in clean vertical arrangement
- Each item: icon/number + bold label + brief description (one line)
- Optional: checkbox icons, priority indicators (stars/colors/badges)
- Clear visual separation between items (spacing or subtle divider lines)
- Scannable design with clear hierarchy
```

---

### 3.8 图表扩展指南

新增图表类型时：

1. 定义清晰的**识别关键词**（用于 `auto` 模式自动判断）
2. 编写**内容结构提示**（指导 AI 如何组织信息）
3. 编写**Prompt 指引片段**（可直接插入模板的英文描述）
4. 在§3.x 中追加新章节

---

## 四、输出场景注册表

### 4.1 场景索引表

| 场景标识符 | 场景名称 | 比例 | 分辨率 | 适用平台 |
|-----------|---------|------|--------|---------|
| `article-16-9` | 文章配图（横版） | 16:9 | 1792x1024 | 博客、文档、公众号 |
| `social-3-4` | 社交媒体竖版 | 3:4 | 768x1024 | 小红书、Instagram Story |
| `social-1-1` | 社交媒体方版 | 1:1 | 1024x1024 | Instagram Post、微信分享 |
| `slide-16-9` | 幻灯片 | 16:9 | 1920x1080 | PPT、演示文稿 |

---

### 4.2 文章配图 (`article-16-9`)

**设计适配建议**：
- 横向构图，左右信息平衡
- 文字适中，考虑在线阅读清晰度
- 留白充足，避免拥挤
- 适合内嵌在长文中，不干扰阅读流

**Prompt 参数片段**：

```
Aspect ratio: 16:9 (1792x1024 pixels)
Layout: horizontal composition, balanced left-right distribution
Text size: medium, optimized for online reading
Whitespace: generous margins and breathing room
```

---

### 4.3 社交媒体竖版 (`social-3-4`)

**设计适配建议**：
- 纵向构图，信息上下流动
- 标题在顶部或上三分之一，必须醒目
- 关键信息在中心区域（拇指热区）
- 底部可留品牌标识或补充信息

**Prompt 参数片段**：

```
Aspect ratio: 3:4 (768x1024 pixels)
Layout: vertical composition, top-to-bottom information flow
Title placement: top third area, bold and attention-grabbing
Key content: center zone (thumb zone for mobile viewing)
Bottom space: optional branding or supplementary info
```

---

### 4.4 社交媒体方版 (`social-1-1`)

**设计适配建议**：
- 居中对称构图
- 核心信息放在中心圆形区域（防止裁切）
- 四角可用于次要信息或装饰
- 适合快速浏览，信息密度中等

**Prompt 参数片段**：

```
Aspect ratio: 1:1 (1024x1024 pixels)
Layout: centered, symmetrical composition
Core content: within central circular safe zone (to avoid cropping on various platforms)
Corners: secondary info or decorative elements
Information density: medium, optimized for quick browsing
```

---

### 4.5 幻灯片 (`slide-16-9`)

**设计适配建议**：
- 横向构图，考虑投影或大屏显示
- 字体更大，远距离可读
- 对比度高，适合明暗不同的投影环境
- 可含标题区和内容区分隔

**Prompt 参数片段**：

```
Aspect ratio: 16:9 (1920x1080 pixels)
Layout: horizontal, designed for projection or large displays
Text size: large, legible from distance (minimum 24pt equivalent)
Contrast: high, suitable for various lighting conditions
Structure: optional title bar at top, main content area below
```

---

### 4.6 场景扩展指南

新增输出场景时：

1. 在§4.1 索引表中添加一行
2. 新增章节包含：
   - **设计适配建议**（3-5条布局和设计指导）
   - **Prompt 参数片段**（比例、分辨率、布局描述）
3. 确保 Prompt 片段可直接插入模板

---

## 五、Atomic Prompting 方法论

### 5.1 四层结构总览

Atomic Prompting 将 Prompt 设计分为四个层级，从宏观到微观逐层细化：

| 层级 | 英文名 | 中文名 | 职责 | 示例维度 |
|------|-------|-------|------|---------|
| L1 | Organism | 基础场景 | 定义主题、调性、核心传达 | 「桌游回合流程教学图」 |
| L2 | Molecule | 细节细化 | 关键信息元素、信息层级、图表类型 | 「3步流程 + 2条补充规则」 |
| L3 | Atomic | 精细细节 | 色彩编码、标签文字、布局规则、字体 | 「黄色=激活状态，标签≤5字」 |
| L4 | Parameters | 技术参数 | 图像比例、色彩方案、渲染风格、输出格式 | 「16:9, Notion风格, PNG」 |

---

### 5.2 Organism Level（基础场景）

**定义内容**：
- **主题**：这张图要讲什么？
- **核心传达**：读者看完要理解什么？
- **调性**：轻松/严肃？新手友好/专业向？

**输出格式**：

```markdown
### Organism Level（基础场景）
- **主题**：{主题描述}
- **核心传达**：{核心信息}
- **调性**：{调性关键词}
```

---

### 5.3 Molecule Level（细节细化）

**定义内容**：
- **关键信息元素**：图中要包含哪些内容模块？
- **信息层级**：主次关系如何？
- **图表类型**：流程图/对比图/列表？
- **图形元素**：图标、人物、箭头、卡片等

**输出格式**：

```markdown
### Molecule Level（细节细化）
- **关键信息元素**：{元素列表}
- **信息层级**：{主体} → {次要}
- **图表类型**：{图表类型名称}
- **图形元素**：{元素列表}
```

---

### 5.4 Atomic Level（精细细节）

**定义内容**：
- **色彩编码**：哪些元素用什么颜色？
- **标签文字**：具体的文字内容（遵循风格限制）
- **布局**：顶部/中部/底部分别放什么？
- **字体**：标题加粗？标签常规？

**输出格式**：

```markdown
### Atomic Level（精细细节）
- **色彩编码**：{颜色=含义}
- **标签文字**：{标签列表}
- **布局**：{布局描述}
- **字体**：{字体规范}
```

---

### 5.5 Parameters Level（技术参数）

**定义内容**：
- **图像比例**：16:9 / 3:4 / 1:1
- **色彩方案**：主色 + 辅色（HEX 或色彩名）
- **渲染风格**：Notion 涂鸦 / 科技感 / 水彩 / 线稿
- **输出格式**：信息图 / 流程图 / 概念图

**输出格式**：

```markdown
### Parameters Level（技术参数）
- **图像比例**：{比例}（{分辨率}）
- **色彩方案**：{色彩描述}
- **渲染风格**：{风格名称}
- **输出格式**：{格式类型}
```

---

## 六、Prompt 组装流程

### 6.1 输入处理

**步骤**：

1. 读取 `DOCUMENT_FILE_PATH` 指定的文件内容
2. 根据 `chapter` 参数定位到对应章节
3. 根据 `extract_mode` 提取内容：
   - `auto`：智能识别章节边界（标题到下一个同级标题）
   - `manual`：用户通过 `custom_instructions` 提供具体内容摘要
   - `full-chapter`：提取整章所有内容

**输出**：`chapter_content`（待分析的原始内容）

---

### 6.2 内容分析

**步骤**：

1. **识别图表类型**（如果 `chart_type` 为 `auto`）：
   - 扫描 `chapter_content` 中的关键词（参见§3各图表类型的识别关键词）
   - 匹配度最高的图表类型作为候选
   - 如无法明确识别，默认使用「列表图」(`checklist`)

2. **提取核心信息**（对应 Atomic L1-L2）：
   - 主题：章节标题或 `chapter` 参数
   - 核心传达：章节第一段或摘要
   - 关键信息元素：根据图表类型提取（步骤、要点、对比项等）

3. **生成 Atomic 四层说明**：
   - Organism：主题 + 核心传达 + 调性
   - Molecule：信息元素 + 层级 + 图表类型 + 图形元素
   - Atomic：色彩编码 + 标签文字 + 布局 + 字体
   - Parameters：比例 + 色彩方案 + 风格 + 格式

**输出**：`atomic_design_notes`（中文四层结构说明）

---

### 6.3 参数组装

**步骤**：

1. 根据 `style_preset` 加载风格预设（§2）的 **Prompt 插槽片段**
2. 根据 `chart_type`（或自动识别结果）加载图表指引（§3）的 **Prompt 指引片段**
3. 根据 `output_scene` 加载场景参数（§4）的 **Prompt 参数片段**
4. 合并 `custom_instructions`（如果提供）
5. 如果 `primary_color` 覆盖了默认主色，在风格片段中替换颜色值

**输出**：`assembled_params`（包含所有 Prompt 片段的参数集）

---

### 6.4 Prompt 生成

**步骤**：

1. 使用通用 Prompt 模板（§7.1）
2. 替换 `{CHART_TYPE_INTRO}`：根据图表类型生成开场描述
3. 替换 `{THEME}`：章节名称或主题
4. 替换 `{STYLE_SLOT}`：风格预设的 Prompt 插槽片段
5. 替换 `{CONTENT_DESCRIPTION}`：从章节内容提炼的具体描述
6. 替换 `{CHART_STRUCTURE_SLOT}`：图表类型的 Prompt 指引片段（填充具体标签）
7. 替换 `{LANGUAGE}`：语言要求
8. 替换 `{SCENE_SLOT}`：输出场景的 Prompt 参数片段
9. 执行质量检查（§8）

**输出**：`final_prompt`（完整的英文 Prompt 字符串）

---

### 6.5 输出保存

**步骤**：

1. 生成文件名：`prompt-{i}.md`
2. 按输出规范（§9.3）组织文件内容
3. 保存到 `./doc-images/prompt-{i}.md`
4. 返回文件路径和生成摘要

---

## 七、通用 Prompt 模板

### 7.1 模板骨架

```
{CHART_TYPE_INTRO} about {THEME}.

{STYLE_SLOT}

{CHART_STRUCTURE_SLOT}

Content:
{CONTENT_DESCRIPTION}

Language: {LANGUAGE}

{SCENE_SLOT}
```

**说明**：
- `{CHART_TYPE_INTRO}`：图表类型开场白，如 "Minimalist hand-drawn doodle-style infographic illustrating..." / "A clean vertical flow chart showing..."
- `{THEME}`：主题/章节名称
- `{STYLE_SLOT}`：风格预设的 Prompt 插槽片段（从§2加载）
- `{CHART_STRUCTURE_SLOT}`：图表结构指引（从§3加载，填充具体内容）
- `{CONTENT_DESCRIPTION}`：具体内容描述（从章节提取或用户提供）
- `{LANGUAGE}`：语言要求（默认 "Chinese preferred, English for technical terms only"）
- `{SCENE_SLOT}`：输出场景参数（从§4加载）

---

### 7.2 风格插槽填充规则

根据 `style_preset` 参数，从§2对应章节加载 **Prompt 插槽片段** 完整插入。

示例（`notion-doodle`）：

```
Style: Minimalist hand-drawn doodle-style infographic.
- Pure white background, zero texture
- Line: 2-4px uniform thickness, clean geometric shapes
- Colors: primary yellow (#FFD93D) with solid fills, high contrast
- Doodle aesthetic: Notion-style relaxed and energetic (do NOT show style description text in image)
- Text: Chinese sans-serif font, only 3-5 character keywords per label, no long sentences
- Simple stick-figure characters if needed (round head, dot/line features, exaggerated relaxed limbs)
- Generous whitespace, breathing room
- No gradients, no 3D effects, no shadows, no textures, no patterns
```

---

### 7.3 图表插槽填充规则

根据 `chart_type` 参数，从§3对应章节加载 **Prompt 指引片段**，并将占位符替换为具体内容。

示例（`flowchart` + 具体内容）：

```
Content structure: Vertical flow chart with 3 steps.
- Start point clearly marked at top
- Each step in rounded rectangle with number badge
- Connecting arrows with clear downward direction
- Step 1 label: "抽牌", description: drawing one card from deck
- Step 2 label: "出牌", description: placing one card face-up
- Step 3 label: "执行能力", description: activating card ability
- Bottom section: two supplementary rules with icons
```

---

### 7.4 场景插槽填充规则

根据 `output_scene` 参数，从§4对应章节加载 **Prompt 参数片段** 完整插入。

示例（`article-16-9`）：

```
Aspect ratio: 16:9 (1792x1024 pixels)
Layout: horizontal composition, balanced left-right distribution
Text size: medium, optimized for online reading
Whitespace: generous margins and breathing room
```

---

## 八、质量检查清单

生成的 Prompt 在输出前必须通过以下检查：

### 8.1 参数完整性检查

- [ ] 必填参数（DOCUMENT_FILE_PATH, chapter, i）均已提供且有效
- [ ] 文档文件存在且可读取
- [ ] 章节名称在文档中能够定位
- [ ] 风格预设 `style_preset` 存在于§2.1 索引表
- [ ] 图表类型 `chart_type` 存在于§3 或为 `auto`
- [ ] 输出场景 `output_scene` 存在于§4.1 索引表

### 8.2 风格一致性检查

- [ ] 风格插槽内容与 `style_preset` 匹配
- [ ] 如提供 `primary_color` 覆盖，已正确替换风格预设中的主色
- [ ] 禁止项（如 Notion 风格的"渐变、3D"）已在 Prompt 中明确声明

### 8.3 可读性检查

- [ ] Prompt 总长度 < 2000 字符（避免过长导致模型理解困难）
- [ ] 具体内容描述清晰，无歧义，非空
- [ ] 标签文字符合风格规范（Notion 风格 3-5字，其他风格酌情）
- [ ] 语言要求明确（"Chinese preferred" / "All text in Chinese"）

### 8.4 输出规范检查

- [ ] Prompt 英文语法基本正确，无明显拼写错误
- [ ] Atomic 四层设计说明完整（Organism/Molecule/Atomic/Parameters）
- [ ] 输出文件命名符合规范（`prompt-{i}.md`）
- [ ] 文件内容结构符合§9.3 定义

**任意一项未通过**：返回检查失败信息，指明具体问题，要求修正后重新生成。

---

## 九、输出文件规范

### 9.1 文件命名规则

```
prompt-{i}.md
```

- `{i}`：由参数 `i` 提供的序号（正整数，如 `1`, `2`, `10`）
- 文件扩展名：`.md`（Markdown 格式）

---

### 9.2 存储路径

```
{工作目录}/doc-images/prompt-{i}.md
```

- 相对于工作目录的 `doc-images/` 文件夹
- 如文件夹不存在，自动创建
- 如文件已存在（同 `i` 值），覆盖前提示用户确认

---

### 9.3 文件内容结构

```markdown
# {主题/文档名} — {章节名} 配图 Prompt

> 目标：为 {文档名} 的 {章节名} 章节生成一张 {风格名} 风格 {图表类型}

---

## Prompt（英文版，适用于 Gemini 3 Image Pro）

```
{FINAL_PROMPT}
```

---

## 设计说明

### Organism Level（基础场景）
- **主题**：{主题}
- **核心传达**：{核心传达}
- **调性**：{调性}

### Molecule Level（细节细化）
- **关键信息元素**：{关键信息元素}
- **信息层级**：{信息层级}
- **图表类型**：{图表类型}
- **图形元素**：{图形元素}

### Atomic Level（精细细节）
- **色彩编码**：{色彩编码}
- **标签文字**：{标签文字列表}
- **布局**：{布局说明}
- **字体**：{字体规范}

### Parameters Level（技术参数）
- **图像比例**：{比例}（{分辨率}）
- **色彩方案**：{色彩方案}
- **渲染风格**：{渲染风格}
- **输出格式**：{输出格式}
```

**说明**：
- 标题行：`#` 一级标题，包含主题和章节名
- 引用块：`>` 简短描述生成目标
- Prompt 代码块：三个反引号包裹，无语言标识符
- 设计说明：四个三级标题（`###`），分别对应 Atomic 四层
