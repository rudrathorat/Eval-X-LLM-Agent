# Eval-X — Offline AI Assistant

A minimalist, offline-first AI interface powered by open-source LLMs.  
Fast, private, and built to run without paid APIs or internet connectivity.

> **Built by Rudra Thorat**

---

## 🚀 Overview

Eval-X is an offline AI assistant that runs entirely on local hardware using open-source models like **LLaMA 3**. It removes reliance on cloud APIs, reduces cost, and provides complete data privacy while serving as a clean, interview-ready demonstration of modern AI engineering.

---

## 🔧 Key Features

- 100% offline (no tokens, no internet required)
- Runs **LLaMA 3 locally using Ollama**
- Backend powered by **LangChain + FastAPI**
- Minimalist UI using HTML + Vanilla JS
- Designed for:
  - CSV input and bulk queries
  - Document parsing
  - RAG-based retrieval
  - Local evaluation use cases

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| LLM Engine | LangChain + Ollama |
| Frontend | HTML + CSS + JavaScript |
| Local Model | LLaMA 3 (Ollama) |
| Server | Uvicorn |

## 📁 Project Structure

```text
📂 Eval-X
├── 🧩 api.py            # FastAPI backend
├── 🤖 model.py          # LangChain + Ollama logic
├── 🎨 templates
│   └── index.html       # Frontend UI
├── 📁 static            # (optional) Styles + scripts
└── 🔧 venv              # Python virtual environment

```
## ⚙️ Installation & Setup

### **1. Clone Repository**
```
git clone <your-repo-url>
cd Eval-X
```

2. Create Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Install Ollama & Pull Model
```
brew install ollama
ollama run llama3
```

4. Start the App
```
uvicorn api:app --reload
```

Open in browser:
```
http://127.0.0.1:8000
```

## 🛠 How It Works

### `api.py`
- Serves the frontend UI
- Exposes the `/evaluate` endpoint to process user queries

### `model.py`
- Wraps LangChain logic
- Executes inference locally using ChatOllama
- No external API calls or cloud dependencies

---

## 🎨 UI Philosophy

- Minimal black-and-white theme
- Fully responsive layout across devices
- Designed with a clean, 2026-inspired aesthetic
- Subtle branding: *"Built by Rudra"* included in the UI

---

## 🔮 Roadmap

- [x] CSV upload support
- [x] Local session memory
- [ ] RAG with local embeddings
- [ ] Export chat to PDF
- [ ] Light/Dark theme toggle
- [ ] Multiple open-source model selection

---

## 💡 Why Eval-X?

- No reliance on OpenAI or paid API keys
- Fully private inference running locally
- Faster experimentation without rate limits
- Ideal for demos, offline workflow, and interview showcases

> *Eval-X proves that intelligent systems can be local, elegant, and fully under your control.*

---

## 👤 Author

**Rudra Thorat**  
AI & Data Science Engineer  
GitHub: [https://github.com/rudrathorat](https://github.com/rudrathorat)
