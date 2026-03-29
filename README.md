# RAG-Powered Translation Assistant

**Improving Translation Workflows with Retrieval-Augmented Generation (RAG) using Proprietary Data**

A full-stack web application developed during an internship at **TOPPAN Nexus, Hong Kong**, that enhances translation quality by combining Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) and proprietary company data.

---

## 🎯 Project Overview

This project explores and implements **Retrieval-Augmented Generation (RAG)** to significantly improve the accuracy, consistency, and domain-specific quality of machine translations. By leveraging internal proprietary documents, glossaries, and previous translations, the system provides context-aware suggestions that outperform standard translation APIs alone.

Key innovation: Combining the strengths of **DeepL** (for high-quality base translation) with **LLM-powered RAG** (for terminology consistency and domain knowledge).

## ✨ Features

- **Retrieval-Augmented Generation (RAG)** pipeline using company-specific data
- Integration with **DeepL API** for high-quality initial translations
- Integration with **LLM APIs** (OpenAI / Anthropic / Groq / etc.) for post-editing and refinement
- Intelligent retrieval from proprietary knowledge base (documents, glossaries, translation memory)
- Full-stack web interface for interactive translation
- Side-by-side comparison between standard translation and RAG-enhanced translation
- Clean and responsive UI for professional use

## Tech Stack

### Backend
- **Python**
- **LlamaIndex** / **LangChain** (RAG framework)
- **Flask**

### Frontend
- **React.js**
- Modern UI framework (Tailwind CSS / Material-UI / etc.)

### APIs
- **DeepL API**
- Multiple LLM providers (01.AI, Mistral, Qwen LLM, etc.)
