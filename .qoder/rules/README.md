---
trigger: always_on
---
# rules/

> 本文件由 qoder-readme-maintainer 自动维护，最后更新：2026-03-09
> 维护状态：✅ 已同步

## 概述

存放项目的规则与规范文件，涵盖写作风格、流程管控、图像生成、数据管理等方面，供 Agent 和 Skill 在执行时引用。

## 文件清单

| 文件名 | 功能描述 | 关键特性 | 依赖关系 | 维护状态 |
|--------|---------|---------|---------|---------|
| ai-human-collaboration.md | 定义 AI 与人类的协作决策框架 | 互为假肢模型、可验证性矩阵、任务评估清单 | - | ✅ |
| article-image-prompt-generator.md | 规范文章配图 Prompt 的生成流程 | 多风格预设、多图表类型、Atomic Prompting 四层方法论 | ← 依赖 notion-style-infographic.md（Notion 风格参考） | ✅ |
| boardgame-rule-structure.md | 规范桌游规则的结构化整理 | 15 个标准模块、素材预处理、新手友好写作 | - | ✅ |
| notion-style-infographic.md | 规范 Notion 官方插画风格信息图生成 | 极简手绘涂鸦风、色彩规范、Prompt 模板 | → 被 article-image-prompt-generator.md 引用 | ✅ |
| short-video-script.md | 规范短视频脚本创作的三段式结构 | 冲突开场、好奇驱动、反转结局、分镜模板 | ← 依赖 writing-style.md（语气参考） | ✅ |
| stage-data-management.md | 规范多阶段工作流的数据管理 | 结果直出+过程收纳、跨阶段传递、摘要必备 | → 被 boardgame-orchestrator Agent 引用 | ✅ |
| title-crafting.md | 规范标题拟定的方法论 | 五大核心技巧、五条思考路径、价值观红线 | ← 配合 writing-style.md、writing-process.md 使用 | ✅ |
| topic-library-standards.md | 规范选题库的数据结构与质量标准 | 单条选题必备字段、分类标准、标题模板规范 | → 被 xiaohongshu-boardgame-analyzer Skill 引用 | ✅ |
| version-control.md | 规范文件夹版本管理策略 | v{N}_{MMDD} 命名、不可覆盖、catalog.md | → 被 boardgame-orchestrator Agent 引用 | ✅ |
| writing-process.md | 规范结构化写作的四阶段流程 | 定位→构思→写作→自检、质量门禁 | ← 配合 writing-style.md 使用 | ✅ |
| writing-style.md | 规范写作风格与表达语气 | 三条铁律、凤头猪肚豹尾、语气红绿灯 | → 被 writing-process.md、short-video-script.md 引用 | ✅ |
| xiaohongshu-content-analysis.md | 规范小红书内容分析的采集与计算标准 | 数据采集频率、标题公式识别、互动分计算 | → 被 xiaohongshu-boardgame-analyzer Skill 引用 | ✅ |

## 依赖关系图

**写作相关**：`writing-style.md` ↔ `writing-process.md` ↔ `title-crafting.md`（互相配合）

**图像相关**：`notion-style-infographic.md` → `article-image-prompt-generator.md`（被引用为子风格）

**工作流相关**：`stage-data-management.md` + `version-control.md` → `boardgame-orchestrator` Agent

**分析相关**：`xiaohongshu-content-analysis.md` + `topic-library-standards.md` → `xiaohongshu-boardgame-analyzer` Skill

## 变更记录

| 日期 | 变更类型 | 文件 | 说明 |
|------|---------|------|------|
| 2026-03-09 | 初始化 | README.md | 首次自动生成目录摘要 |
