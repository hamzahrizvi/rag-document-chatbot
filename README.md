# RAG Document Chatbot (v2)

## Overview

A local Retrieval-Augmented Generation (RAG) chatbot that allows users to upload documents and query their contents. Version 2 introduces persistent storage, removing the need to re-upload documents each session.

## What’s New (v2)

- Persistent vector database (FAISS saved locally)
- Documents processed once and reused across sessions
- Faster startup after initial indexing
- Improved retrieval consistency

## Features

- Document ingestion (.txt)
- Text chunking and embeddings
- Semantic search with FAISS
- Context-aware responses using Ollama
- Local execution (no external APIs)
- Persistent knowledge base

## Architecture

```text
Upload Document (once)
        |
        v
Chunk + Embed
        |
        v
Save Vector Store (local)
        |
        v
User Query
        |
        v
Load Vector Store
        |
        v
Similarity Search
        |
        v
LLM Response
````

## Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* Ollama

## How to Run

```bash
conda create -n rag-env python=3.10 -y
conda activate rag-env
pip install -r requirements.txt
```

Start model:

```bash
ollama run phi
```

Run app:

```bash
streamlit run app.py
```

## Notes

* First run will process and store embeddings locally
* Subsequent runs reuse stored data (no re-upload needed)

## Next Improvements

* PDF support
* Multi-file ingestion
* Chat history and memory
* Source citations

```

---

### What changed vs v1
- explicitly mentions **persistence**
- removes unnecessary explanation
- focuses on **what improved**
- more “engineering-style” (better for recruiters)

---

```
