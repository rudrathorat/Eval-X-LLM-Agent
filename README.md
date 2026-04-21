# Eval-X

Eval-X is a lightweight local AI web app built with FastAPI, Ollama, and a simple HTML frontend. It lets you ask general questions to a locally running `llama3` model and upload a CSV so you can ask questions about that dataset in the same interface.

> Built by Rudra Thorat

## Overview

This project is a local-first prototype for running an AI assistant without depending on paid cloud APIs. The app serves a browser UI, accepts user questions, sends prompts to an Ollama-hosted `llama3` model, and supports a basic CSV-aware workflow.

Right now, the project is best understood as:

- a local LLM demo app
- a CSV question-answering prototype
- a foundation for a more advanced offline assistant

## What It Currently Does

- Runs a FastAPI backend
- Serves a simple browser UI
- Sends user questions to a locally running `llama3` model through Ollama
- Lets the user upload a CSV file
- Loads the uploaded CSV into memory with pandas
- Uses the first 10 rows of the uploaded CSV as prompt context when answering data-related questions

## What It Does Not Yet Do

The current codebase does not yet implement:

- true RAG or vector retrieval
- document parsing for PDFs or other file types
- persistent chat/session memory
- multi-user isolation
- advanced dataframe querying or analytics
- model selection from the UI

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| LLM Integration | LangChain + Ollama |
| Frontend | HTML + CSS + JavaScript |
| Data Handling | pandas |
| Local Model | `llama3` via Ollama |
| Server | Uvicorn |

## Project Structure

```text
Eval-X
├── api.py
├── model.py
├── eval_engine.py
├── templates/
│   └── index.html
├── csv_data/
│   └── ajanta_sample_data.csv
└── README.md
```

## How It Works

### `api.py`

- Serves the frontend at `/`
- Exposes `POST /evaluate` for text questions
- Exposes `POST /upload_csv` for CSV uploads
- Saves uploaded CSV files into `csv_data/`

### `model.py`

- Connects to Ollama using `ChatOllama(model="llama3")`
- Stores the most recently uploaded CSV in memory
- Builds a prompt from the uploaded CSV preview plus the user's question
- Falls back to a general question-answer flow if no CSV has been uploaded

### `templates/index.html`

- Renders the UI
- Sends questions to `/evaluate`
- Uploads CSVs to `/upload_csv`
- Displays the model response in the page

### `eval_engine.py`

- Contains a second Ollama prompt wrapper
- Is currently not used by `api.py`

## Current Behavior Notes

- Only the most recently uploaded CSV is kept in memory
- CSV reasoning is prompt-based, not true structured analysis
- The model only sees a preview of the dataset, not the full CSV in a queryable engine
- This app is currently better suited for local demos or single-user use than public multi-user deployment

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Eval-X
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

Install the packages used in the codebase:

```bash
pip install fastapi uvicorn jinja2 python-multipart pandas langchain langchain-community langchain-ollama
```

### 4. Install and run Ollama with `llama3`

```bash
ollama run llama3
```

Make sure Ollama is running locally before starting the app.

### 5. Start the server

```bash
uvicorn api:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Use Cases

- Local AI demo without cloud APIs
- Private CSV question-answering on a single machine
- Portfolio project demonstrating local LLM integration
- Starting point for a document assistant or internal self-hosted AI tool

## Limitations

- No authentication
- No persistent storage for chat history
- No user/session separation
- Uploaded CSV context is limited and in-memory only
- Public hosting would require additional production hardening

## Why This Project Is Useful

Eval-X turns a raw local model runtime into a usable application flow. Instead of talking to Ollama directly in the terminal, a user gets a browser interface, a backend API, CSV upload support, and prompt orchestration in one place.

That makes the project useful as both:

- a working prototype of a private local AI assistant
- a base for building a more capable offline or self-hosted AI product

## Author

**Rudra Thorat**  
GitHub: [https://github.com/rudrathorat](https://github.com/rudrathorat)
