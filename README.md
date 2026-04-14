# RAG Document Chatbot (v2)

## Overview

A local Retrieval-Augmented Generation (RAG) chatbot that allows users to upload documents and query their contents.  
Version 2 introduces persistent storage, improved retrieval quality, and more reliable response generation.

---

## Key Improvements (v2)

- Persistent local vector database (FAISS)
- Documents indexed once and reused across sessions
- Separation of LLM and embedding models
- Improved retrieval accuracy using dedicated embedding model
- Reduced hallucinations through stricter prompt design
- Context-aware answer generation (not just extraction)
- Query-type handling (credentials vs procedural questions)
- Basic performance monitoring (retrieval + LLM timing)

---

## Architecture

```text
Upload Document (once)
        |
        v
Chunking (smaller segments)
        |
        v
Embeddings (nomic-embed-text)
        |
        v
Vector Store (FAISS - persisted locally)
        |
        v
User Query
        |
        v
Similarity Search (top-k chunks)
        |
        v
Context + Query → LLM (mistral-nemo)
        |
        v
Response Generation
```
## Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- Ollama

## Running the Project
conda create -n rag-env python=3.10 -y
conda activate rag-env
pip install -r requirements.txt

## Pull required models:

ollama pull mistral-nemo
ollama pull nomic-embed-text

## Run the app:
streamlit run app.py

## Notes
- Vector store must be rebuilt after changing embedding models
- Retrieval quality depends on chunking and document structure
- Local model performance depends on available system resources

## Next Steps
- Multi-file ingestion
- PDF support
- Source attribution in answers
- Chat history and memory
- UI improvements

---
