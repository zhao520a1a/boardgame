# agents/

> 本文件由 qoder-readme-maintainer 自动维护，最后更新：2026-03-09
> 维护状态：✅ 已同步

## 概述

存放 AI Agent 定义文件，Agent 作为智能编排器调度多个子 Skill 协同完成复杂工作流。

## 文件清单

| 文件名 | 功能描述 | 关键特性 | 依赖关系 | 维护状态 |
|--------|---------|---------|---------|---------|
| boardgame-orchestrator.md | 编排桌游图文笔记创作全流程，调度 7 个子 Skill | 意图识别、智能决策、记忆进化、上下文传递 | → 被 skills/ 下所有 boardgame-* Skill 协作调用 | ✅ |

## 依赖关系图

```
boardgame-orchestrator
  ├── boardgame-input-collector (阶段1)
  ├── xiaohongshu-boardgame-analyzer (独立/可选)
  ├── boardgame-rule-graphic (阶段2/可选)
  ├── boardgame-cover-design (阶段3)
  ├── boardgame-inner-pages (阶段4)
  ├── boardgame-copywriting (阶段5)
  ├── boardgame-posting-strategy (阶段6)
  └── boardgame-publisher (阶段7/可选)
```

关联规则文件：`stage-data-management.md`、`version-control.md`、`ai-human-collaboration.md` 等（位于 rules/）。

## 变更记录

| 日期 | 变更类型 | 文件 | 说明 |
|------|---------|------|------|
| 2026-03-09 | 初始化 | README.md | 首次自动生成目录摘要 |
