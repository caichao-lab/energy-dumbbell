# Changelog

All notable changes to the Energy Dumbbell Marketing System knowledge base.

---

## [6.2] - 2026-08-14

### 🎉 Initial Public Release

**First open-source release** — complete knowledge base publicly available.

### Added

#### Core Knowledge Base (`dist/01_core/`)
- 6.2 纯净版完整加载包（单文件启动入口）
- 底层系统提示词（主文件）
- R 规则库（完整推理规则链）
- T 术语库（全域术语定义）
- P / Q / S / SBF 四维决策矩阵
- 全局联动规则 & 风控规则
- 导图校准层 & 节点映射表
- 电商术语全集（抖音电商、线上线下运营）
- 配套补全文档（库1库2对照、资源复制层约束等）

#### Case Library (`dist/02_cases/`)
- C 案例库（综合经营矛盾推演案例）
- I 行业矩阵（实体/电商/私域行业适配）
- 电商决策战法（抖音电商推演模板）
- 电商映射简化导图

#### Archive (`dist/03_archive/`)
- 6.2 完整版导图（母版）
- 1.0 - 12.0 营销导图迭代表

#### 3D Visual Models (`assets/visual-models/`)
- 7 Three.js interactive HTML models:
  - `flipmap_standard.html` - 标准翻转导图
  - `flipmap_with_strategy.html` - 含策略标注翻转导图
  - `glass_top_ball_chaos.html` - 双层球酒杯模型（标准版）
  - `glass_top_noball_chaos.html` - 带顶去外层球
  - `glass_notop_noball_chaos.html` - 无顶无球极简版
  - `glass_grid_standard.html` - 线框网格教学版
  - `glass_grid_hetero.html` - 哑铃异构体（高阶理论）

#### Demo Code (`demo/`)
- `config_example.json` - 配置示例
- `quick_start.py` - 快速启动演示脚本
- `rag_ingest.py` - RAG 知识库导入演示（分块 + 统计）
- `demo_README.md` - Demo 使用说明

#### Documentation
- README.md / README_EN.md - 中英文首页
- INDEX.md - 完整目录索引（位于 `docs/`）
- Term_Glossary.md - 中英术语对照表
- LICENSE.md - CC BY-NC-ND 4.0 许可证

#### Full Source Archive (`src/`)
- `00_顶层体系概述/` - 8 篇体系哲学与架构文档
- `01_AI推理源库/` - 完整多层推理原稿（含 7 个子目录）
- `04_开发&运维手册/` - 3 份迭代维护文档
- `99_internal_workspace/` - 内部工作区
  - 迭代规则素材库（草稿/话术/自查清单）
  - 历史版本备份存档（ASCII 树形图 23 个 + PDF 24 个）
  - 历史交付样品（2 个旧版启动包）

---

## [6.1] - 2026-06-xx

> Internal development version. Not publicly released.

- 迭代更新台账建立
- 轻量化口语问诊话术初版
- 闲聊模式 Prompt 初版

---

## [5.4] - 2026-04-xx

> Internal development version. Not publicly released.

- 早期 93 条 R 规则链版本
- V12.1-LLM 体系基础框架

## 🙏 致谢

感谢您关注能量哑铃营销体系 V6.2。这是作者多年商业推理实践的沉淀。
虽然 V6.2 已停止迭代，但它凝聚了体系最初的完整思考脉络。
如果您在经营诊断中发现了新的逻辑边界，欢迎提 Issue 交流。