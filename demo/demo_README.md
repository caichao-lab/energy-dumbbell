# demo/ — 演示代码使用说明

> 本目录包含配套 dist 知识库的 Python 演示代码，供开发者参考和二次开发。

---

## 📂 文件列表

| 文件 | 说明 |
|:---|:---|
| `config_example.json` | 配置文件示例（路径、模型参数） |
| `quick_start.py` | 极简启动演示（读取单文件启动包） |
| `rag_ingest.py` | RAG 导入演示（扫描 + 分块 + 统计） |
| `demo_README.md` | 本文件 |

---

## 🚀 quick_start.py

**作用**：演示如何读取 `dist/01_core/` 中的启动包，对接兼容 OpenAI 格式的大模型 API。

**使用步骤**：
1. 复制 `config_example.json` 为 `config.json`
2. 填入你的 API Key 和模型名称
3. 运行 `python quick_start.py`
4. 在终端输入经营问题，查看 AI 响应

**依赖**：
```bash
pip install openai
## 📊 rag_ingest.py

**作用**：演示如何扫描 `dist/01_core/` 和 `dist/02_cases/` 中的 Markdown 文件，按标题（`##` / `###`）分块，输出统计报告和样本 JSON。

**使用步骤**：
```bash
python rag_ingest.py
```

**输出**：
- 终端显示统计报告（文件数、块数、字符数）
- 生成 `demo/chunks_sample.json` 供人工检查分块效果

**依赖**：**无需安装任何额外依赖**（仅使用 Python 标准库）

**说明**：本脚本仅做演示分块，未实际向量化入库。如需完整 RAG 落地，请参考输出提示自行接入 ChromaDB / Pinecone / LanceDB 等向量数据库。

---

## ⚙️ config_example.json 字段说明

```json
{
  "base_url": "https://api.openai.com/v1",
  "api_key": "your-api-key-here",
  "model": "gpt-4",
  "system_prompt_path": "../dist/01_core/6.2纯净版完整加载包(单文件_新对话首条).md"
}
```

| 字段 | 说明 |
|:---|:---|
| `base_url` | API 地址（支持 OpenAI / 兼容接口） |
| `api_key` | 你的 API Key |
| `model` | 模型名称 |
| `system_prompt_path` | 启动包文件路径（相对于 `demo/` 目录） |

---

## 💡 极简使用 vs 完整 RAG

| 模式 | 文件 | 说明 |
|:---|:---|:---|
| 极简试用 | `quick_start.py` + 单文件启动包 | 本地快速测试，无需向量库 |
| 完整 RAG | `rag_ingest.py` + 全部 `dist/01_core/` | 需要自行接入向量数据库 |

---

## ⚠️ 注意事项

1. 本目录代码**仅供学习参考**，未做生产级容错处理
2. 实际商用部署请完善错误处理、日志、安全校验
3. API Key 请勿提交到 Git 仓库（建议使用环境变量）