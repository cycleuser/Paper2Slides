# Paper2Slides (Local Edition)

[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)

> 本项目是 [Paper2Slides](https://github.com/HKUDS/Paper2Slides) 的一个**定制分支 (Fork)**，旨在为希望保护隐私或降低成本的用户提供**完全的本地模型 (Ollama) 支持**。

---

## 📖 关于本分支

原版 Paper2Slides 是一个非常出色的项目，能够利用 GPT-4o 等先进模型生成高质量的幻灯片。然而，许多用户希望能够在本地运行整个流程，以确保数据隐私或避免昂贵的 API 费用。

**本分支并未对原项目的核心逻辑进行重大增强**，而是专注于以下**适配工作**：

1.  **Ollama 原生支持**：重构了底层 LLM 调用逻辑，使其能直接连接本地运行的 Ollama 服务。
2.  **多模型协作配置**：引入了更细致的配置系统，允许用户分别为“对话”、“视觉”和“嵌入”任务指定不同的本地模型（如 Llama3, LLaVA, Nomic）。
3.  **HTML 降级模式**：针对本地模型无法生成高质量图片的问题，增加了 HTML 输出模式，确保在没有 DALL-E 的情况下也能产出可用的演示文稿。

我们非常感谢 **HKUDS** 团队开源了如此优秀的原项目。如果您追求极致的生成效果且不介意使用云端 API，推荐您直接使用[原版 Paper2Slides](https://github.com/HKUDS/Paper2Slides)。

---

## ⚠️ 本地版局限性声明

使用本地模型（尤其是 7B/8B 规模的小模型）与使用 GPT-4o 相比，客观上存在差距：

1.  **逻辑能力**：小模型在长文档的逻辑梳理和总结上可能不如商业大模型严谨。
2.  **视觉生成**：本分支**移除了对 AI 绘图的强依赖**。如果在配置中未提供绘图 API Key，系统将生成**图文 HTML 幻灯片**（使用原论文配图），而不会尝试 AI 绘画。
3.  **速度**：本地推理速度取决于您的显卡性能。

---

## 🚀 快速上手 (Ollama 版)

### 1. 环境准备

```bash
# 克隆本分支
git clone https://github.com/cycleuser/Paper2Slides.git
cd Paper2Slides

# 创建环境
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置本地模型

我们编写了一个简单的脚本来帮助您快速生成配置文件：

```bash
# 确保您已安装 Ollama 并 pull 了相关模型 (如 llama3, llava, nomic-embed-text)
python scripts/setup_ollama.py
```

或者手动创建 `paper2slides/.env` 文件：

```bash
# paper2slides/.env 推荐配置 (Qwen3 组合)

LLM_PROVIDER=ollama
# 主模型：负责思考和写作
LLM_MODEL=qwen3:4b-instruct
# 视觉模型：负责看图
VISION_MODEL=qwen3-vl:2b
# 嵌入模型：负责搜索
EMBEDDING_MODEL=qwen3-embedding:4b
EMBEDDING_DIM=768

# 连接设置
RAG_LLM_BASE_URL=http://localhost:11434/v1
RAG_LLM_API_KEY=ollama

# 留空以使用 HTML 模式 (不进行 AI 绘图)
IMAGE_GEN_API_KEY=
IMAGE_GEN_BASE_URL=
```

### 3. 运行

```bash
# 生成 HTML 幻灯片
python -m paper2slides --input paper.pdf --output slides
```

---

## 📁 主要改动

相较于原版，本分支主要修改了以下文件以适配本地环境：
- `paper2slides/rag/config.py`: 增加了对 Ollama 及多模型配置的支持。
- `paper2slides/utils/llm.py`: 新增统一的 LLM 客户端工厂。
- `paper2slides/generator/image_generator.py`: 新增 HTML 降级生成逻辑。
- `scripts/setup_ollama.py`: 新增交互式配置脚本。

---

## 🙏 致谢

再次感谢原作者团队的杰出工作：
- **[Paper2Slides (Upstream)](https://github.com/HKUDS/Paper2Slides)**
- **[LightRAG](https://github.com/HKUDS/LightRAG)**
- **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)**

如果您觉得本分支对您在本地部署有帮助，也请不吝给原项目点个 Star ⭐️。
