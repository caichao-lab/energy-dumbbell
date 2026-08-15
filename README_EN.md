# 🏋️ Energy Dumbbell Marketing System · 6.2

[中文版本](./README.md) | English

> A structured business marketing diagnosis knowledge base for LLMs — turning AI from a "chat assistant" into a "professional business consultant."

---

## ⚠️ Important Notice

This repository **does NOT contain complete production application code**.

The core asset is an original closed-loop commercial reasoning knowledge ontology (Markdown structured documents), designed to build marketing decision agents.

You can import all documents into **Dify, FastGPT, LangChain, local LLMs, self-developed Agent frameworks**, or any compatible LLM platform.

The `/demo` folder provides minimal Python scripts **for demonstration only** — not production-ready, not mandatory, with no technical stack restrictions.

📖 Full repository index: [INDEX.md](docs/INDEX.md)  
📖 Official term glossary: [Term_Glossary.md](./Term_Glossary.md)

📖 [Project positioning, Demo explanation, common misconceptions → supplemental notes](docs/README_DETAIL.md)

This repository focuses on continuously improving **business reasoning rules, theoretical models, strategy library, terminology library, and deduction cases**.

---

## 📦 Project Overview

Most open-source marketing AI resources are fragmented prompts, single role instructions, or generic marketing theories — relying on opaque black-box reasoning, prone to hallucinations, and difficult to trace.

This project delivers an **independently developed, iterated dynamic dialectical commercial reasoning system**, powered by multi-rule constraints and a built-in marketing mind map module. It combines quantifiable retrieval with assisted reasoning to automate commercial marketing decision-making. It is a complete self-developed system with fully traceable outputs.

Built on original models (V6.2 core models): **Operation Entity, Idle Entity, Energy Dumbbell Structure Model, Wine Glass Model, Internal & External Dual-Factor Interference Model, Problem-Strategy Dual-List Reasoning Architecture, and Profit Regulator Valve Model**. It covers the full marketing reasoning chain: product, customer, transaction, profit, idle asset activation, and strategy pool matching. It helps small and micro-business owners tackle common operational pain points with targeted, scientific, and actionable strategy plans — effectively reducing overall marketing costs.

---

## 📂 Repository Structure

| Directory | Description | Audience |
|:---|:---|:---|
| `dist/01_core/` | Core inference knowledge base (required) — includes one-file quick-start package | All users |
| `dist/02_cases/` | Case study enhancement (optional) | Users needing industry examples |
| `dist/03_archive/` | Archived materials (human reference only, not for RAG) | Users interested in evolution history |
| `assets/visual-models/` | 3D visual architecture models (HTML) | Users who want to visualize the model |
| `demo/` | Python demo code | Developers for customization |
| `src/` | Raw development materials (drafts/archives) | Deep researchers, system iterators |

---

## 📚 Supplemental Repository Notes

### 1. Project Basics
This repository is the V6.2 historical archive of the Energy Dumbbell Marketing System. Total compressed package size is 4.17 MB, all in Markdown format (plus mind maps in TXT and PDF).

This version was finalized in July 2026 as a transitional release. A next-generation inference engine has been fully refactored and will be published in a separate repository. **This repository will not receive further updates.**

### 2. Version Evolution
The system traces its roots back to the original *Shang Shen Marketing Science* and the *Scientific Selling* series, evolving through multiple iterations to become the Energy Dumbbell Marketing System. V6.2 employs white-box rule-framework reasoning, suitable for testing, debugging, and research. Early V6.2 versions have known limitations — such as insufficient strategy coverage, weak closed-loop reasoning, lack of weighted strategy prioritization, and incomplete diagnostic input integration. Exercise caution when deploying directly in production AI systems.

### 3. Source Directory Guide (`src/`)
- `顶层体系概述/` — Theory and philosophy (human reading only, not for AI)
- `AI推理库/` — Full inference materials for deep development
- `内部素材库/` — Drafts and work-in-progress (not calibrated, **do not use for formal diagnosis**)
- `开发&运维手册/` — Version iteration specifications (for developers)
- `历史版本备份存档/` — V6.1 archives (reference only, do not use commercially)

### 4. File Selection Recommendations
- Deep development: Use the full package at `src/AI推理库/`
- Quick start for beginners: Use `dist/01_core/6.2纯净版完整加载包(单文件_新对话首条).md`
- ⚠️ Do not mix launch packages from different sources — rule validation standards may differ

---

## 🚀 30-Second Quick Start

**The simplest way:**

1. Open any one of the following large language models: ChatGPT, Claude, Doubao, DeepSeek, Kimi, or Qwen.  
2. Locate the file `6.2纯净版完整加载包(单文件_新对话首条).md` in the `dist/01_core/` directory.  
3. Select all, copy the content, paste it into a new chat dialog, and send it to confirm.  
4. Wait for the model to finish reading, then manually type or voice‑input your specific business question in the dialog.  
5. The model will automatically reason and output a complete strategic diagnostic report and solution plan.

> 💡 No installation, no API configuration — one file is all you need.

---

## 🔧 How to Choose Between the Three Startup Packages

- **Full Version** (recommended for beginners): `dist/01_core/6.2纯净版完整加载包(单文件_新对话首条).md` — Copy and use, supports mode switching
- **Lite Demo Version**: Suitable for quick consultations and offline client acquisition
- **Professional Diagnosis Version**: Suitable for enterprise clients, financing presentations, and in-depth diagnostics

---

## 📊 Three Diagnostic Modes

### 1. Full Diagnostic Mode (Default)
On first use, the system enters Full Diagnostic Mode by default and will guide you through a business information questionnaire. Provide a detailed description of your store or business, and the full diagnostic process begins.

### 2. Quick Diagnostic Mode
If you don't have specific business data and prefer not to answer the questionnaire step by step, simply type **"skip"**, **"quick mode"**, or **"direct analysis"**. The system will immediately skip the questionnaire and generate a rapid diagnosis based on available information.

### 3. E-Commerce Mode
E-commerce users can type **"e-commerce mode"** to switch to an E-Commerce Diagnostic Mode, which outputs e-commerce-specific strategy plans.

### 4. Generate a Complete Report
After the diagnostic dialogue, type **"report"** to merge all outputs into a detailed, comprehensive report.

---

## 👥 Three Usage Modes

### ① Quick Trial (Recommended for Beginners)
- Load ONLY `6.2纯净版完整加载包(单文件_新对话首条).md`
- Copy-paste and go — no deployment needed
- Best for: quick demos, personal consultations, trying out the system

### ② Full RAG Deployment (Recommended for Production)
- Import ALL files from `dist/01_core/` into Dify / FastGPT / LangChain
- Enables rule constraints, unified terminology, multi-dimensional strategy matching
- Best for: enterprise-grade AI agents, formal diagnosis systems

### ③ Deep Learning / Custom Development
- Read `src/顶层体系概述/` to understand the underlying philosophy
- Explore `src/AI推理源库/` for the complete creative process
- View `assets/visual-models/` for 3D architecture visualization
- Best for: researchers, system iterators, developers

---

## 🙋 FAQ

**Q: I'm a brick-and-mortar store owner with no technical background. Can I use this?**  
A: Yes. Simply copy the contents of the `.md` file into any LLM chat window.

**Q: I'm a developer. I want to build my own RAG agent. Which files should I use?**  
A: Import all files from `dist/01_core/` and refer to the example code in `demo/`.

**Q: Why are there drafts and old versions in the `src/` directory?**  
A: `src/` contains the complete original development assets for deep researchers. Regular users should use the `dist/` production packages.

---

## 🍷 3D Visual Models

| Model Description | Chinese | English | Use Case |
|:---|:---|:---|:---|
| 🥂 Double Sphere Standard Edition (Default) | [中文](assets/visual-models/glass_top_ball_chaos.html) | [English](assets/visual-models/glass_top_ball_chaos_en.html) | Full market + operations dual-layer architecture |
| 📐 Wireframe Teaching Edition | [中文](assets/visual-models/glass_grid_standard.html) | [English](assets/visual-models/glass_grid_standard_en.html) | Clear structural outline, ideal for screenshots & presentations |
| 💪 Dumbbell Hetero Edition (Advanced Theory) | [中文](assets/visual-models/glass_grid_hetero.html) | [English](assets/visual-models/glass_grid_hetero_en.html) | Shows product/customer push-pull balance logic |
| 🔄 Flip Mind Map (with Strategy Labels) | [中文](assets/visual-models/flipmap_with_strategy.html) | [English](assets/visual-models/flipmap_with_strategy_en.html) | View strategy node distribution samples |
| 🍷 Wine Glass · Outer Rings Removed (Simplified) | [中文](assets/visual-models/glass_top_noball_chaos.html) | [English](assets/visual-models/glass_top_noball_chaos_en.html) | Highlights internal structure without outer ring interference |
| 🍷 Wine Glass · Minimalist (No Top, No Rings) | [中文](assets/visual-models/glass_notop_noball_chaos.html) | [English](assets/visual-models/glass_notop_noball_chaos_en.html) | Minimalist version for beginners to grasp core structure |
| 🌳 Flip Mind Map · Pure CSS (Standard) | [中文](assets/visual-models/flipmap_standard.html) | [English](assets/visual-models/flipmap_standard_en.html) | Standard flip mind map showing basic framework |

---

## 📌 Attribution & Brand Usage Guidelines (MIT License Supplement)

The 3D visual models in this repository (located in `assets/visual-models/`) are original works. Under the MIT License (with copyright notice retained), you are free to use, modify, and commercialize them.

**We encourage you to:**
- ✅ Prominently credit the model author: "3D Model Author: Zhang Dabao"
- ✅ Contribute improvements back to this repository

**We kindly ask you to:**
- ❌ Do not imply that the model is your own original creation (retain the original author credit)
- ❌ Do not use the models for illegal or unethical purposes

**Commercial Customization:** For custom color schemes, interactive customizations, or enterprise licensing, please contact Zhang Dabao — commercial customization pricing is lower than the cost of developing from scratch.

---

## 📜 Copyright & Open Source License

All documents in this repository are open-sourced under the **MIT License** for personal learning and technical exchange.

- ✅ Permitted: Learning, research, non-commercial modification, internal use
- ❌ Prohibited: Without the author's written authorization, packaging and selling the complete knowledge base as a commercial product, reselling, or using it in paid SaaS services

---

## 📌 Version Notice & Open Source Scope

This repository is an **archived release of Energy Dumbbell Marketing System V6.2**. A next-generation inference engine has been deeply refactored and upgraded based on this framework and is under continuous independent development. It is **not included** in this repository.

**"Energy Dumbbell Marketing System V6.2"** — the complete knowledge ontology (including mind maps, rule matrices, inference workflows, terminology libraries, strategy libraries, and 3D visual models) — is original intellectual property of **Zhang Dabao**.

---

## ⚠️ Disclaimer

1. This framework provides standardized business diagnosis reasoning logic only. It does not constitute financial, legal, or industry compliance advice. Please consult professionals for implementation.
2. This repository contains early drafts and obsolete files. Users must distinguish valid documents themselves. The author assumes no responsibility for business losses caused by misuse of deprecated materials.
3. V6.2 is a historical transitional version with inherent reasoning limitations. It should not be used directly as a production-grade commercial AI backend — for architectural learning and reference only.

---

## 📥 Download Mirrors

- **Primary source (recommended)**: Clone from GitHub / Gitee
- **Alternative mirrors (full 4.17 MB compressed package)**:
  - **Aliyun Drive**: https://www.alipan.com/s/SDtrDn5CSgu
  - **Quark Drive**: https://pan.quark.cn/s/68946b332736

---

## 📦 Repository Info

- **Version**: 6.2 (historical archive, no further updates)
- **Updated**: 2026-08-14
- **Compressed package size**: 4.17 MB
- **Format**: All Markdown text
- **Gitee平台**：https://gitee.com/caichao-lab/energy-dumbbell
- **Github平台**：https://github.com/caichao-lab/energy-dumbbell

---

## 📧 Feedback & Contributions

- Submit Issues: Report problems or suggest improvements
- Submit Pull Requests: Contribute code or documentation enhancements
- 📮 Contact the author: [caichao-lab@foxmail.com](mailto:caichao-lab@foxmail.com) (Business cooperation, custom consulting, system licensing)
