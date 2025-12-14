# Paper2Slides (Local Edition)

[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)

> This project is a **customized fork** of [Paper2Slides](https://github.com/HKUDS/Paper2Slides), dedicated to providing **full local model (Ollama) support** for privacy-conscious users.

---

## 📖 About This Fork

The original Paper2Slides is an excellent project capable of generating high-quality presentations using advanced models like GPT-4o. However, many users prefer running the entire pipeline locally to ensure data privacy or avoid API costs.

**This fork does not significantly enhance the core logic of the original project.** Instead, it focuses on **adaptation**:

1.  **Native Ollama Support**: Refactored the underlying LLM calls to directly connect with local Ollama instances.
2.  **Multi-Model Configuration**: Introduced a granular configuration system, allowing different local models for "Chat", "Vision", and "Embedding" tasks (e.g., Llama3, LLaVA, Nomic).
3.  **HTML Fallback Mode**: Added an HTML output mode to address the inability of local models to generate high-quality images, ensuring usable slides without DALL-E.

We are deeply grateful to the **HKUDS** team for open-sourcing such a great project. If you prioritize maximum generation quality and don't mind using cloud APIs, we highly recommend using the [Original Paper2Slides](https://github.com/HKUDS/Paper2Slides).

---

## ⚠️ Limitations of Local Edition

Compared to GPT-4o, using local models (especially small 7B/8B ones) has objective limitations:

1.  **Reasoning**: Small models may be less rigorous in structuring and summarizing long documents.
2.  **Visual Generation**: This fork **removes the hard dependency on AI image generation**. If no Image Gen API Key is provided, the system generates **text-based HTML slides** (using original paper figures) instead of attempting AI painting.
3.  **Speed**: Inference speed depends entirely on your local GPU performance.

---

## 🚀 Quick Start (Ollama)

### 1. Environment

```bash
# Clone this fork
git clone https://github.com/cycleuser/Paper2Slides.git
cd Paper2Slides

# Create environment
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Local Models

We provide a script to help you generate the config file:

```bash
# Ensure Ollama is running and models are pulled (e.g., llama3, llava, nomic-embed-text)
python scripts/setup_ollama.py
```

Or manually create `paper2slides/.env`:

```bash
# paper2slides/.env Recommended (Qwen3 Combo)

LLM_PROVIDER=ollama
# Brain: Reasoning & Writing
LLM_MODEL=qwen3:4b-instruct
# Eyes: Vision & Charts
VISION_MODEL=qwen3-vl:2b
# Memory: Search & RAG
EMBEDDING_MODEL=qwen3-embedding:4b
EMBEDDING_DIM=768

# Connection
RAG_LLM_BASE_URL=http://localhost:11434/v1
RAG_LLM_API_KEY=ollama

# Leave blank to use HTML Mode (No AI Painting)
IMAGE_GEN_API_KEY=
IMAGE_GEN_BASE_URL=
```

### 3. Run

```bash
# Generate HTML Slides
python -m paper2slides --input paper.pdf --output slides
```

---

## 📁 Key Changes

Compared to upstream, this fork mainly modified:
- `paper2slides/rag/config.py`: Added support for Ollama and multi-model config.
- `paper2slides/utils/llm.py`: Added unified LLM client factory.
- `paper2slides/generator/image_generator.py`: Added HTML fallback logic.
- `scripts/setup_ollama.py`: Added interactive setup script.

---

## 🙏 Acknowledgements

Thanks again to the original authors for their outstanding work:
- **[Paper2Slides (Upstream)](https://github.com/HKUDS/Paper2Slides)**
- **[LightRAG](https://github.com/HKUDS/LightRAG)**
- **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)**

If this fork helps your local deployment, please consider giving the original project a Star ⭐️.
