# Paper2Slides: 一键从论文生成演示文稿

[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)

✨ **从此告别从零制作 PPT** ✨

| 📄 **通用文档支持** &nbsp;|&nbsp; 🎯 **RAG 增强精准度** &nbsp;|&nbsp; 🤖 **本地模型支持 (Ollama)** &nbsp;|&nbsp; 🎨 **自定义风格** |

---

## 🎯 什么是 Paper2Slides?

Paper2Slides 能够在几分钟内将您的**研究论文**、**报告**和**文档**转化为**专业级的幻灯片 (Slides) 和海报 (Poster)**。

### ⚠️ 本地模型使用提示

本项目支持通过 **Ollama** 运行本地模型（如 Llama3, Qwen2 等），这提供了极佳的隐私保护且完全免费。但请注意：

1.  **生成效果差异**：本地小参数模型（如 7B/8B 版本）在逻辑推理、长文本总结和指令遵循能力上，可能不如 GPT-4o 等商业闭源模型。您可能会遇到幻灯片逻辑稍显简单或排版不够精美的情况。
2.  **视觉生成限制**：Ollama 目前主要专注于文本和多模态理解，**不具备直接生成高质量幻灯片图片的能力**。
    - 当未配置外部绘图 API (如 DALL-E) 时，系统会自动切换到 **HTML 降级模式**。
    - 该模式下，系统会生成包含文字和原论文配图的 HTML 幻灯片，而非 AI 绘制的图片。

### ✨ 核心特性

- 🤖 **全面支持本地大模型 (Ollama)**
  原生支持 Ollama，利用本地 LLM (Llama3, Qwen2 等) 处理文本，视觉模型 (LLaVA) 处理图表，嵌入模型 (Nomic) 处理检索，实现数据完全私有化运行。

- 📄 **通用文档支持**
  无缝处理 PDF、Word、Excel、PowerPoint、Markdown 等多种格式。
  
- 🎯 **深度内容提取**
  基于 RAG (检索增强生成) 技术，精准捕获每一个关键观点、数据和图表。
  
- 🔗 **源文溯源**
  生成内容可直接追溯至原文，消除信息偏差。
  
- ⚡ **极速生成**
  支持快速预览模式和并行生成，大幅提升效率。

---

## 🏃 快速开始

### 1. 环境准备

```bash
# 克隆仓库
git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides

# 创建并激活 conda 环境
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# 安装依赖
pip install -r requirements.txt
```

### 2. 模型配置 (推荐)

Paper2Slides 现在支持通过 **Ollama** 使用本地模型，同时也支持 **OpenAI** 和 **通义千问 (Qwen)**。

我们提供了一个交互式脚本来帮助您快速配置：

```bash
# 运行配置向导 (需确保已安装并运行 Ollama)
python scripts/setup_ollama.py
```

该脚本会自动检测您本地已安装的 Ollama 模型，并引导您选择：
1. **主模型 (Main LLM)**: 用于逻辑推理和文本生成 (如 `llama3`, `qwen2.5`)
2. **视觉模型 (Vision Model)**: 用于理解论文中的图表 (如 `llava`, `moondream`)
3. **嵌入模型 (Embedding Model)**: 用于 RAG 检索 (如 `nomic-embed-text`)

**或者**，您可以手动创建 `paper2slides/.env` 文件并修改：

```bash
# paper2slides/.env 示例 (Ollama + Qwen3 组合推荐)

# Provider Selection
LLM_PROVIDER=ollama

# Model Configuration
LLM_MODEL=qwen3:4b-instruct
VISION_MODEL=qwen3-vl:2b
EMBEDDING_MODEL=qwen3-embedding:4b
EMBEDDING_DIM=768

# Connection Settings
RAG_LLM_BASE_URL=http://localhost:11434/v1
RAG_LLM_API_KEY=ollama

# Image Generation (OpenRouter / OpenAI)
# 留空将使用 HTML 降级模式（推荐本地用户）
IMAGE_GEN_API_KEY=
IMAGE_GEN_BASE_URL=
```

### 3. 运行生成

```bash
# 生成幻灯片 (默认)
python -m paper2slides --input paper.pdf --output slides

# 生成海报 (指定风格)
python -m paper2slides --input paper.pdf --output poster --style "minimalist blue"

# 极速模式 (跳过 RAG 索引，适合短文)
python -m paper2slides --input paper.pdf --fast
```

---

## 🔧 详细配置指南

为了获得最佳效果，Paper2Slides 采用了**多模型协作**架构。在 `.env` 文件中，您可以精细控制每个环节使用的模型：

| 配置项 | 作用 | 推荐模型 (Ollama) | 推荐模型 (OpenAI) |
|--------|------|-------------------|-------------------|
| `LLM_MODEL` | **大脑**：负责理解全文、规划大纲、总结内容 | `llama3`, `qwen2.5`, `mistral` | `gpt-4o` |
| `VISION_MODEL` | **眼睛**：负责看懂论文中的插图、图表和数据 | `llava`, `llama3.2-vision` | `gpt-4o` |
| `EMBEDDING_MODEL` | **记忆索引**：负责将文本转化为向量以供检索 | `nomic-embed-text`, `mxbai-embed-large` | `text-embedding-3-large` |

### 支持的提供商 (Provider)

通过 `.env` 中的 `LLM_PROVIDER` 切换：

- **`ollama`**: 本地私有化部署，免费且隐私安全。无需 API Key。
- **`openai`**: 使用官方 API，效果最佳。需配置 `RAG_LLM_API_KEY`。
- **`qwen`**: 使用阿里云 DashScope API (通义千问)，性价比高，中文能力强。需配置 `RAG_LLM_BASE_URL` 和 `RAG_LLM_API_KEY`。

---

## 🏗️ 架构原理

Paper2Slides 包含 4 个核心阶段，确保从输入到输出的高质量转换：

| 阶段 | 描述 | 关键技术 |
|------|------|----------|
| **1. 🔍 RAG (检索)** | 解析文档，构建向量索引 | `EMBEDDING_MODEL` |
| **2. 📊 分析 (Analysis)** | 提取文档结构，识别关键图表 | `VISION_MODEL` |
| **3. 📋 规划 (Planning)** | 规划演示文稿的逻辑流和页面布局 | `LLM_MODEL` |
| **4. 🎨 创作 (Creation)** | 渲染最终的视觉页面 | 图像生成 API 或 HTML 模板 |

---

## 📁 代码结构

```
Paper2Slides/
├── paper2slides/
│   ├── core/                 # 核心流水线 (Pipeline)
│   ├── rag/                  # RAG 引擎 (配置、客户端、查询)
│   ├── generator/            # 内容生成与规划
│   ├── summary/              # 内容提取 (摘要、图表)
│   └── utils/                # 通用工具 (含统一 LLM 客户端)
├── scripts/
│   └── setup_ollama.py       # Ollama 交互式配置脚本
├── api/                      # 后端 API 服务
└── frontend/                 # React 前端界面
```

---

## 🙏 致谢

本项目基于以下开源项目构建：
- **[LightRAG](https://github.com/HKUDS/LightRAG)**: Graph-Empowered RAG
- **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)**: Multi-Modal RAG

---

<div align="center">
❤️ 觉得有用？请给我们点个 Star ⭐️！
</div>
