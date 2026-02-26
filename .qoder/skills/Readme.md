

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
├── content-writing/               ← 通用内容创作
│   └── SKILL.md
├── text-to-infographic/           ← 通用文本可视化信息图（独立）
│   └── SKILL.md
└── critical-thinking-challenger/  ← 通用批判性思维辅助（独立）
    └── SKILL.md
```

### 设计原则

| 原则 | 实现方式 |
|------|---------|
| **Agent + Skill** | `boardgame-orchestrator` Agent 作为智能编排器，调度 6 个子 Skill |
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
