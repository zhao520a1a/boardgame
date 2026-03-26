

## 架构概览 - Agent + Skill 协同体系

```
.qoder/agents/
└── boardgame-orchestrator.md      ← 智能编排 Agent（总控）

.qoder/skills/
├── boardgame-input-collector/     ← 阶段1：前置输入收集
│   └── SKILL.md
├── boardgame-rule-graphic/        ← 阶段2：规则讲解图（可选）
│   └── SKILL.md
├── boardgame-cover-design/        ← 阶段3：封面图生成
│   └── SKILL.md
├── boardgame-inner-pages/         ← 阶段4：内页图生成
│   └── SKILL.md
├── boardgame-copywriting/         ← 阶段5：文案撰写
│   └── SKILL.md
├── boardgame-posting-strategy/    ← 阶段6：发帖策略+热点适配
│   └── SKILL.md
├── boardgame-publisher/           ← 阶段7：半自动发布到小红书
│   └── SKILL.md
├── boardgame-story-extractor/      ← 独立：实战字幕故事提炼
│   └── SKILL.md
├── xiaohongshu-boardgame-analyzer/ ← 独立：小红书内容分析与选题
│   └── SKILL.md
├── content-writing/               ← 通用内容创作
│   └── SKILL.md
├── text-to-infographic/           ← 通用文本可视化信息图（独立）
│   └── SKILL.md
├── critical-thinking-challenger/  ← 通用批判性思维辅助（独立）
│   └── SKILL.md
└── qoder-readme-maintainer/       ← 维护：.qoder 目录 README 自动维护
    └── SKILL.md
```

### 设计原则

| 原则 | 实现方式 |
|------|---------|
| **Agent + Skill** | `boardgame-orchestrator` Agent 作为智能编排器，调度 7 个子 Skill |
| **单一职责** | 每个 Skill 只负责一个阶段，独立完整 |
| **智能决策** | Agent 根据用户自然语言自动判断执行哪些阶段 |
| **记忆迭代** | Agent 记住用户偏好和历史，优化未来推荐 |
| **插件式组合** | 可全流程执行，也可单独调用任意阶段 |
| **上下文传递** | 通过标准化「上下文摘要」在阶段间传递数据 |

### 调用方式

- **智能编排**（推荐）：直接对话，Agent 自动理解意图并决策
  ```
  帮我做《璀璨宝石》的小红书笔记
  ```
- **带参数启动**：提供部分或全部参数
  ```
  桌游名称：《璀璨宝石》
  推广目标：涨粉
  风格偏好：文艺调性
  具体规则： ​情书规则.txt​ 
  图片素材： ​素材​ 
  ```
- **单独阶段**：直接调用任意子 Skill
  ```
  /boardgame-cover-design
  /boardgame-copywriting
  ```
- **迭代修改**：自然语言描述修改需求
  ```
  封面换成高点击率风格
  标题再换几个
  ```
- **独立 Skill**：不经过编排器，直接调用
  ```
  /text-to-infographic 情书/情书规则_新版.txt
  ```

---

> 以下由 qoder-readme-maintainer 自动维护，最后更新：2026-03-09

## Skill 文件清单

| 文件夹 | 功能描述 | 关键特性 | 依赖关系 | 状态 |
|--------|---------|---------|---------|------|
| boardgame-input-collector/ | 收集桌游笔记创作的前置输入信息 | 结构化提问、标准化上下文摘要 | → 输出供后续所有阶段使用 | ✅ |
| boardgame-rule-graphic/ | 生成桌游规则一页纸可视化速查图 | 国际通用教学框架、768×1024 | ← 依赖 input-collector 上下文 | ✅ |
| boardgame-cover-design/ | 生成 3 张不同风格的桌游笔记封面 | 文艺调性/高点击率/人物产品、A/B 测试 | ← 依赖 input-collector 上下文 | ✅ |
| boardgame-inner-pages/ | 生成 4 张内页（教学/解析/场景/技巧） | 完整滑动阅读体验、风格与封面统一 | ← 依赖 cover-design 封面风格 | ✅ |
| boardgame-copywriting/ | 撰写小红书风格的标题、正文和 Hashtag | 4 种标题公式、6 段正文结构、热点适配 | ← 依赖 input-collector 上下文 | ✅ |
| boardgame-posting-strategy/ | 提供发帖策略和 A/B 测试方案 | 发布时间建议、评论区运营 | ← 依赖 copywriting 文案输出 | ✅ |
| boardgame-publisher/ | 半自动发布笔记到小红书创作者平台 | 浏览器自动填充、A/B 版本管理 | ← 依赖所有前序阶段输出 | ✅ |
| boardgame-story-extractor/ | 从实战视频字幕提炼活人感故事片段 | 翻译式提炼、6类故事分类、多人对话 | ← 引用 writing-style + rule-structure 规则 | ✅ |
| xiaohongshu-boardgame-analyzer/ | 分析小红书桌游热门内容并生成选题库 | 浏览器采集、数据分析 | ← 引用 rules/ 下分析规则 | ✅ |
| content-writing/ | 通用内容创作，自动匹配写作模式 | 风格指导/完整流程/组合模式 | ← 引用 rules/ 下写作规则 | ✅ |
| text-to-infographic/ | 将文本文件转为橙白风格信息图 PNG | HTML→截图→PNG、多页/长图 | - | ✅ |
| critical-thinking-challenger/ | 批判性思维辅助，识别推理盲点 | 结构化反馈、多轮深挖 | - | ✅ |
| qoder-readme-maintainer/ | 自动维护 .qoder 目录下各子文件夹 README | 自动/手动/定期触发 | - | ✅ |
