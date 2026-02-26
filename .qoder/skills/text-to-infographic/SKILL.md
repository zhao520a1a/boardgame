---
name: text-to-infographic
description: "通用文本可视化。将 Markdown/TXT 文件转为橙白风格信息图（HTML→浏览器截图→PNG），支持 3:4 多页图和单页长图两种输出模式，交互式预览与迭代修改。当用户提供文本文件并要求生成信息图、知识卡片、规则图解、可视化长图时调用。关键词：信息图、可视化、长图、知识卡片、规则图解。"
---

# 通用文本信息图生成

> 职责：读取结构化文本 → 内容分析 → 生成 HTML 信息图 → 交互式预览 → 用户确认后导出 PNG

---

## 一、参数定义

### 必填参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `source_file` | string | 源文件路径（.md / .txt） |

### 可选参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `output_mode` | `longform` | `longform`（单页长图）/ `multipage`（3:4 多页图） |
| `theme_name` | 从文件名提取 | 主题名，用于标题和文件命名 |

---

## 二、执行流程

```
步骤1: 读取源文件 → 步骤2: 内容分析 → 步骤3: 生成HTML → 步骤4: 预览 → 步骤5: 迭代 → 步骤6: 导出
```

### 步骤 1：读取源文件

1. 读取 `source_file` 内容
2. 自动检测格式（Markdown / 纯文本）
3. 若未指定 `theme_name`，从文件名提取（去除扩展名和路径）

### 步骤 2：内容分析

应用§三的组件映射规则，将文本结构转化为组件列表：

1. **结构识别**：解析 Markdown 语法（标题、列表、表格、引用、粗体）
2. **语义增强**：基于关键词和上下文判断高级组件（flow-box / end-cards / callout 变体）
3. **标题口语化**：将正式标题转为疑问句式（如"游戏组件" → "游戏里有什么？"）
4. **提取元信息**：从文档开头提取副标题和标签关键词

### 步骤 3：生成 HTML

1. 选择容器模式：`longform` → `.card` / `multipage` → `.page`
2. 组装标题区：主标题 + 副标题 + 标签
3. 按组件列表依次渲染各 section
4. 注入§四的完整 CSS
5. 写入 HTML 文件：`{output_dir}/{theme}_信息图.html`

### 步骤 4：预览展示

1. 用 `mcp__browser-use__new_page` 打开 HTML 文件
2. 用 `mcp__browser-use__take_screenshot(fullPage=true)` 截取预览图
3. 展示给用户

### 步骤 5：交互迭代

询问用户是否满意。支持的修改操作：

| 用户指令 | 执行动作 |
|---------|---------|
| "把第N节改成流程图" | 将 item-list 替换为 flow-box |
| "加一个警告提示" | 在指定位置插入 callout.warn |
| "标题改成 xxx" | 修改主标题或章节标题 |
| "删掉第N节" | 移除指定 section |
| "把表格放到第2页" | 调整多页模式分页 |
| "满意了，导出" | 进入步骤 6 |

每次修改后：Edit HTML → `mcp__browser-use__navigate_page(type=reload)` → 重新截图预览。

### 步骤 6：导出

**longform 模式：**
1. `mcp__browser-use__take_screenshot(fullPage=true, filePath={theme}_长图.png)`

**multipage 模式：**
1. `mcp__browser-use__take_snapshot()` → 获取各 `.page` 元素 uid
2. 逐页 `mcp__browser-use__take_screenshot(uid=pageUid, filePath={theme}_P{N}.png)`

输出文件清单给用户。

---

## 三、组件映射规则

### 3.1 结构识别（Markdown → 组件）

| Markdown 语法 | 组件 | HTML class |
|---------------|------|-----------|
| `## 标题` | 编号章节头 | `.section-header` + `.section-num` |
| `### 子标题` | 子标题 | `.sub-title` |
| `- 列表` / `1. 列表` | 勾选清单 | `.item-list` |
| `\| 表格 \|` | 橙色表头表格 | `.info-table` |
| `> 引用` | 提示框 | `.callout` |
| `**粗体**` | 橙色高亮 | `span.em` |

### 3.2 语义增强（上下文 → 高级组件）

| 判断条件 | 组件 | 说明 |
|---------|------|------|
| 有序列表 3-4 项 + 标题含"步骤/流程/操作/顺序" | `.flow-box` | 3步流程卡片+箭头 |
| 引用或段落含"注意/警告/必须/禁止" | `.callout.callout-warn` | 黄色警告框 |
| 引用或段落含"提示/技巧/建议" | `.callout.callout-tip` | 绿色提示框 |
| 两个并列的情况/条件描述 | `.end-cards` | A/B 对比卡片 |
| 文档 META 区的关键词 | `.tags` | 标签胶囊 |

### 3.3 标题口语化转换

将正式标题转换为口语化疑问句：

| 原标题模式 | 转换后 |
|-----------|--------|
| 游戏组件 / 组件 | 游戏里有什么？ |
| 游戏准备 / 设置 / 开局 | 开局怎么准备？ |
| 回合流程 / 玩法 | 轮到我怎么玩？ |
| 结束条件 / 一轮结束 | 一轮怎么结束？ |
| 胜利条件 / 游戏结束 | 谁赢了整场游戏？ |
| 注意事项 / 补充规则 | 注意事项 |
| 变体 / 特殊规则 | 特殊玩法 |

通用公式：当无匹配时，用 `{主题}是什么？` 或 `关于{主题}` 格式。

### 3.4 主标题生成

```
一次性讲清楚<span class="highlight">{theme_name}</span>规则
```

副标题从 META 区提取（如人数、时长、类型），用 ` | ` 分隔。

---

## 四、完整 CSS

生成 HTML 时，将以下完整 CSS 嵌入 `<style>` 标签。

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  background: #f5f5f5;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  gap: 20px;
}

/* ══ longform 单页容器 ══ */
.card {
  width: 440px;
  background: #ffffff;
  border-radius: 12px;
  padding: 36px 30px 40px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
}

/* ══ multipage 分页容器 ══ */
.page {
  width: 768px;
  height: 1024px;
  background: #ffffff;
  padding: 36px 36px 28px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
}
.page-content { flex: 1; display: flex; flex-direction: column; }
.page-num {
  position: absolute;
  bottom: 14px;
  right: 28px;
  font-size: 12px;
  color: #ccc;
  font-weight: 500;
}
.page-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 18px;
  padding-bottom: 12px;
  border-bottom: 2px solid #F5A623;
}
.page-header-icon {
  width: 32px; height: 32px;
  background: #F5A623;
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
}
.page-header-text {
  font-size: 20px;
  font-weight: 700;
  color: #333;
}
.spacer { flex: 1; }

/* ══ 标题区 ══ */
.title-area {
  text-align: center;
  margin-bottom: 28px;
}
.title-area h1 {
  font-size: 26px;
  font-weight: 900;
  color: #1a1a1a;
  letter-spacing: 2px;
  margin-bottom: 4px;
}
.title-area h1 .highlight {
  background: linear-gradient(180deg, transparent 50%, #FFD6A0 50%);
  padding: 0 4px;
}
.title-area .subtitle {
  font-size: 13px;
  color: #888;
  margin-top: 6px;
}
.title-area .oneliner {
  font-size: 13px;
  color: #555;
  margin-top: 10px;
  line-height: 1.7;
  padding: 10px 14px;
  background: #FFF8EE;
  border-radius: 8px;
  border-left: 3px solid #F5A623;
}

/* ══ 章节 ══ */
.section { margin-top: 26px; }
.section-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}
.section-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #F5A623;
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.section-title {
  font-size: 17px;
  font-weight: 700;
  color: #1a1a1a;
}

/* ══ 勾选清单 ══ */
.item-list {
  list-style: none;
  padding-left: 0;
}
.item-list li {
  font-size: 13.5px;
  color: #333;
  line-height: 1.75;
  padding: 4px 0 4px 24px;
  position: relative;
}
.item-list li::before {
  content: '\2713';
  position: absolute;
  left: 0;
  color: #F5A623;
  font-weight: 700;
  font-size: 13px;
}
.item-list li .em {
  color: #E08600;
  font-weight: 600;
}

/* ══ 流程步骤 ══ */
.flow-box {
  display: flex;
  gap: 8px;
  margin: 12px 0;
}
.flow-step {
  flex: 1;
  background: #FFF8EE;
  border-radius: 10px;
  padding: 14px 10px;
  text-align: center;
  border: 1px solid #FFE4B5;
}
.flow-step .step-icon {
  font-size: 26px;
  margin-bottom: 6px;
}
.flow-step .step-label {
  font-size: 14px;
  font-weight: 700;
  color: #D4880F;
  margin-bottom: 2px;
}
.flow-step .step-desc {
  font-size: 11.5px;
  color: #777;
  line-height: 1.5;
}
.flow-arrow {
  display: flex;
  align-items: center;
  color: #F5A623;
  font-size: 18px;
  font-weight: 700;
  flex-shrink: 0;
}

/* ══ 表格 ══ */
.info-table {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0;
  font-size: 13px;
}
.info-table th {
  background: #F5A623;
  color: #fff;
  font-weight: 600;
  padding: 8px 12px;
  text-align: center;
  font-size: 12.5px;
}
.info-table th:first-child { border-radius: 6px 0 0 0; }
.info-table th:last-child { border-radius: 0 6px 0 0; }
.info-table td {
  padding: 7px 12px;
  text-align: center;
  color: #444;
  border-bottom: 1px solid #f0f0f0;
}
.info-table tr:nth-child(even) td { background: #FFFAF2; }
.info-table tr:last-child td:first-child { border-radius: 0 0 0 6px; }
.info-table tr:last-child td:last-child { border-radius: 0 0 6px 0; }

/* ══ 提示框 ══ */
.callout {
  background: #FFF3E0;
  border-radius: 8px;
  padding: 12px 14px;
  margin: 12px 0;
  font-size: 13px;
  color: #8B5E00;
  line-height: 1.7;
  display: flex;
  gap: 8px;
  align-items: flex-start;
}
.callout .callout-icon {
  font-size: 16px;
  flex-shrink: 0;
  margin-top: 1px;
}
.callout-warn {
  background: #FFF8E1;
  border: 1px solid #FFE082;
}
.callout-tip {
  background: #E8F5E9;
  border: 1px solid #C8E6C9;
  color: #2E7D32;
}

/* ══ 分隔线 ══ */
.divider {
  border: none;
  border-top: 1px dashed #e0e0e0;
  margin: 24px 0 0;
}

/* ══ 标签 ══ */
.tags {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 6px;
  flex-wrap: wrap;
}
.tag {
  font-size: 11.5px;
  color: #F5A623;
  border: 1px solid #F5A623;
  border-radius: 12px;
  padding: 2px 10px;
  background: #FFFAF2;
}

/* ══ 子标题 ══ */
.sub-title {
  font-size: 14px;
  font-weight: 600;
  color: #D4880F;
  margin: 14px 0 8px;
  padding-left: 2px;
}

/* ══ A/B 对比卡片 ══ */
.end-cards {
  display: flex;
  gap: 10px;
  margin: 10px 0;
}
.end-card {
  flex: 1;
  border-radius: 10px;
  padding: 14px 12px;
  text-align: center;
}
.end-card-a {
  background: #FFF8EE;
  border: 1px solid #FFE4B5;
}
.end-card-b {
  background: #F3F8FF;
  border: 1px solid #C8DEFF;
}
.end-card .ec-icon {
  font-size: 24px;
  margin-bottom: 6px;
}
.end-card .ec-title {
  font-size: 13px;
  font-weight: 700;
  color: #333;
  margin-bottom: 4px;
}
.end-card .ec-desc {
  font-size: 11.5px;
  color: #777;
  line-height: 1.55;
}

/* ══ 页脚 ══ */
.bottom-note {
  text-align: center;
  font-size: 11px;
  color: #bbb;
  margin-top: 24px;
  letter-spacing: 1px;
}
.footer-note {
  text-align: center;
  font-size: 12px;
  color: #bbb;
  margin-top: auto;
  padding-top: 12px;
}

/* ══ multipage 字号适配 ══ */
.page .section-title { font-size: 19px; }
.page .item-list li { font-size: 15px; }
.page .flow-step .step-label { font-size: 16px; }
.page .callout { font-size: 14px; }
.page .info-table { font-size: 14px; }
.page .section-num { width: 30px; height: 30px; font-size: 16px; }
```

---

## 五、HTML 组件模板

生成 HTML 时，按以下模板组装各组件。

### 5.1 文档骨架（longform）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{theme_name} 信息图</title>
<style>
{§四的完整CSS}
</style>
</head>
<body>
<div class="card">
  {title_area}
  {sections_with_dividers}
  <div class="bottom-note">{theme_name} · 信息图</div>
</div>
</body>
</html>
```

### 5.2 文档骨架（multipage）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>{§四的完整CSS}</style>
</head>
<body>
<!-- 第1页 -->
<div class="page" id="page1" role="img" aria-label="page1">
  <div class="page-content">
    {title_area}
    {page1_sections}
    <div class="spacer"></div>
    <div class="footer-note">{theme_name}</div>
  </div>
  <span class="page-num">1 / {total}</span>
</div>
<!-- 第N页 -->
<div class="page" id="pageN" role="img" aria-label="pageN">
  <div class="page-content">
    <div class="page-header">
      <span class="page-header-icon">{首字}</span>
      <span class="page-header-text">{theme_name}</span>
    </div>
    {pageN_sections}
    <div class="spacer"></div>
    <div class="footer-note">{theme_name}</div>
  </div>
  <span class="page-num">N / {total}</span>
</div>
</body>
</html>
```

### 5.3 标题区

```html
<div class="title-area">
  <h1>一次性讲清楚<span class="highlight">{主题关键词}</span>规则</h1>
  <div class="subtitle">{副标题信息}</div>
  <div class="tags">
    <span class="tag">{标签1}</span>
    <span class="tag">{标签2}</span>
  </div>
  <div class="oneliner">{一句话介绍}</div>
</div>
<hr class="divider">
```

### 5.4 编号章节

```html
<div class="section">
  <div class="section-header">
    <div class="section-num">{N}</div>
    <div class="section-title">{口语化标题}</div>
  </div>
  {内容组件}
</div>
<hr class="divider">
```

### 5.5 勾选清单

```html
<ul class="item-list">
  <li><span class="em">{重点}</span> — {说明}</li>
  <li>{普通文本} <span class="em">{高亮词}</span> {后续文本}</li>
</ul>
```

### 5.6 流程步骤（3步）

```html
<div class="flow-box">
  <div class="flow-step">
    <div class="step-icon">{emoji}</div>
    <div class="step-label">{步骤名}</div>
    <div class="step-desc">{描述}</div>
  </div>
  <div class="flow-arrow">&#10132;</div>
  <div class="flow-step"><!-- 同上 --></div>
  <div class="flow-arrow">&#10132;</div>
  <div class="flow-step"><!-- 同上 --></div>
</div>
```

### 5.7 提示框

```html
<!-- 默认提示 -->
<div class="callout">
  <span class="callout-icon">&#128203;</span>
  <span>{提示内容}</span>
</div>

<!-- 警告 -->
<div class="callout callout-warn">
  <span class="callout-icon">&#9888;</span>
  <span><strong>{标题}：</strong>{内容}</span>
</div>

<!-- 技巧 -->
<div class="callout callout-tip">
  <span class="callout-icon">&#128161;</span>
  <span>{提示内容}</span>
</div>
```

### 5.8 数据表格

```html
<table class="info-table">
  <tr><th>{表头1}</th><th>{表头2}</th></tr>
  <tr><td>{数据}</td><td>{数据}</td></tr>
</table>
```

### 5.9 A/B 对比卡片

```html
<div class="end-cards">
  <div class="end-card end-card-a">
    <div class="ec-icon">{emoji}</div>
    <div class="ec-title">{情况A标题}</div>
    <div class="ec-desc">{描述}</div>
  </div>
  <div class="end-card end-card-b">
    <div class="ec-icon">{emoji}</div>
    <div class="ec-title">{情况B标题}</div>
    <div class="ec-desc">{描述}</div>
  </div>
</div>
```

---

## 六、分页规则（multipage 模式）

```yaml
页面尺寸: 768 x 1024 px
页眉区: 80px
页脚区: 60px
可用内容高度: 884px

组件高度估算:
  section-header: 60px
  item-list: 40px x 项数 + 20px
  flow-box: 180px
  callout: 80px + 内容行数 x 24px
  info-table: 40px x 行数 + 30px
  end-cards: 200px 
  divider: 25px

分页策略:
  1. 贪心累加各组件高度
  2. 累计超过 884px 时分页
  3. 单个 section（含其子组件）不可跨页拆分
  4. 首页: 标题区(约200px) + 1-2个section
  5. 续页: page-header + 2-3个section
```

---

## 七、输出规范

```yaml
输出目录: 源文件同级目录下的 output/ 子目录（不存在则创建）

文件命名:
  HTML源文件: "{theme}_信息图.html"
  longform PNG: "{theme}_长图.png"
  multipage PNG: "{theme}_P1.png", "{theme}_P2.png", ...

截图参数:
  longform: fullPage=true
  multipage: 逐个 .page 元素截图（通过 take_snapshot 获取 uid）
```
