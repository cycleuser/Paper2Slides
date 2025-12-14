# Paper2Slides: Generate Presentations from Papers

[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)

✨ **Stop Creating Slides from Scratch** ✨

| 📄 **Universal Doc Support** &nbsp;|&nbsp; 🎯 **RAG Precision** &nbsp;|&nbsp; 🤖 **Local Model Support (Ollama)** &nbsp;|&nbsp; 🎨 **Custom Styles** |

---

## 🎯 What is Paper2Slides?

Paper2Slides transforms your **research papers**, **reports**, and **documents** into **professional slides and posters** in minutes.

### ⚠️ Note on Local Models

This project supports running local models via **Ollama** (e.g., Llama3, Qwen2), offering privacy and free usage. However, please note:

1.  **Generation Quality**: Smaller local models (e.g., 7B/8B) may produce less coherent content or simpler logic compared to large commercial models like GPT-4o.
2.  **Visual Generation Limitations**: Ollama models primarily focus on text and multimodal understanding. They **cannot generate high-quality slide images directly**.
    - If no external image generation API (like DALL-E) is configured, the system automatically switches to **HTML Fallback Mode**.
    - In this mode, it generates HTML slides containing text and original figures from the paper, rather than AI-painted images.

### ✨ Key Features

- 🤖 **Full Local Model Support (Ollama)**
  Natively supports Ollama, using local LLMs (Llama3, Qwen2) for text, vision models (LLaVA) for charts, and embedding models (Nomic) for RAG, ensuring complete data privacy.

- 📄 **Universal Document Support**
  Seamlessly handles PDF, Word, Excel, PowerPoint, Markdown, and more.
  
- 🎯 **Deep Content Extraction**
  Uses RAG (Retrieval-Augmented Generation) to accurately capture key insights, data, and figures.
  
- 🔗 **Source Traceability**
  Generated content can be traced back to the original text, eliminating hallucinations.
  
- ⚡ **Fast Generation**
  Supports fast preview mode and parallel processing for efficiency.

---

## 🏃 Quick Start

### 1. Environment Setup

```bash
# Clone repository
git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides

# Create and activate conda environment
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# Install dependencies
pip install -r requirements.txt
```

### 2. Model Configuration (Recommended)

Paper2Slides supports **Ollama** (Local), **OpenAI**, and **Qwen** (Aliyun).

We provide an interactive script to help you configure quickly:

```bash
# Run setup wizard (Ensure Ollama is installed and running)
python scripts/setup_ollama.py
```

This script detects your local Ollama models and guides you to select:
1. **Main LLM**: For reasoning and text generation (e.g., `llama3`, `qwen2.5`)
2. **Vision Model**: For understanding figures in papers (e.g., `llava`, `moondream`)
3. **Embedding Model**: For RAG retrieval (e.g., `nomic-embed-text`)

**Or**, you can manually create `paper2slides/.env` and modify it:

```bash
# paper2slides/.env Example (Ollama + Qwen3 Recommendation)

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
# Leave blank to use HTML Fallback Mode (Recommended for local users)
IMAGE_GEN_API_KEY=
IMAGE_GEN_BASE_URL=
```

### 3. Run Generation

```bash
# Generate slides (Default)
python -m paper2slides --input paper.pdf --output slides

# Generate poster (Specific style)
python -m paper2slides --input paper.pdf --output poster --style "minimalist blue"

# Fast mode (Skip RAG indexing, good for short papers)
python -m paper2slides --input paper.pdf --fast
```

---

## 🔧 Detailed Configuration

To achieve the best results, Paper2Slides uses a **Multi-Model Collaboration** architecture. You can fine-tune the models in `.env`:

| Config | Role | Recommended (Ollama) | Recommended (OpenAI) |
|--------|------|----------------------|----------------------|
| `LLM_MODEL` | **Brain**: Understands text, plans outline, summarizes | `llama3`, `qwen2.5`, `mistral` | `gpt-4o` |
| `VISION_MODEL` | **Eyes**: Understands figures, charts, and data | `llava`, `llama3.2-vision` | `gpt-4o` |
| `EMBEDDING_MODEL` | **Memory**: Indexes text for retrieval | `nomic-embed-text`, `mxbai-embed-large` | `text-embedding-3-large` |

### Supported Providers

Switch via `LLM_PROVIDER` in `.env`:

- **`ollama`**: Local private deployment, free and secure. No API Key needed.
- **`openai`**: Official API, best performance. Requires `RAG_LLM_API_KEY`.
- **`qwen`**: Aliyun DashScope API, high cost-performance ratio. Requires `RAG_LLM_BASE_URL` and `RAG_LLM_API_KEY`.

---

## 🏗️ Architecture

Paper2Slides consists of 4 core stages:

| Stage | Description | Key Tech |
|-------|-------------|----------|
| **1. 🔍 RAG** | Parse documents, build vector index | `EMBEDDING_MODEL` |
| **2. 📊 Analysis** | Extract structure, identify key figures | `VISION_MODEL` |
| **3. 📋 Planning** | Plan presentation flow and layout | `LLM_MODEL` |
| **4. 🎨 Creation** | Render final visual pages | Image Gen API or HTML Template |

---

## 📁 Project Structure

```
Paper2Slides/
├── paper2slides/
│   ├── core/                 # Core Pipeline
│   ├── rag/                  # RAG Engine (Config, Client, Query)
│   ├── generator/            # Content Generation & Planning
│   ├── summary/              # Content Extraction (Summary, Figures)
│   └── utils/                # Utilities (Unified LLM Client)
├── scripts/
│   └── setup_ollama.py       # Ollama Setup Script
├── api/                      # Backend API
└── frontend/                 # React Frontend
```

---

## 🙏 Acknowledgements

This project is built upon:
- **[LightRAG](https://github.com/HKUDS/LightRAG)**: Graph-Empowered RAG
- **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)**: Multi-Modal RAG

---

<div align="center">
❤️ Found this useful? Give us a Star ⭐️!
</div>
