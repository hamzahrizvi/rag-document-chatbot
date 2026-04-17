# Local Knowledge Assistant (RAG Chatbot)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

A local Retrieval-Augmented Generation (RAG) chatbot that allows users to upload documents and query their contents. The system retrieves relevant context using vector search and generates grounded answers using local LLMs.

This project demonstrates an end-to-end AI application with persistent storage, multi-document support, reranking, and chat memory.

---


## Key Features

### Multi-Document Support
- Upload multiple files in one session
- Supports `.txt`, `.pdf`, and `.docx`

### Persistent Knowledge Base
- Documents are embedded and stored locally (FAISS)
- No need to re-upload after restarting the app

### Model Selection
- Switch between models at runtime:
  - `phi` (fast)
  - `mistral` (balanced)
  - `mistral-nemo` (accurate)

### Improved Retrieval
- Dedicated embedding model: `nomic-embed-text`
- Reranking using cross-encoder for better relevance
- Reduced hallucinations

### Chat Memory
- Maintains recent conversation context
- Enables follow-up questions

### Source Attribution
- Displays source documents for each answer
- Improves transparency and trust

---

## Architecture

```text
Document Upload (multi-file)
        |
        v
Text Extraction (TXT / PDF / DOCX)
        |
        v
Chunking
        |
        v
Embeddings (nomic-embed-text)
        |
        v
FAISS Vector Store (persistent)
        |
        v
User Query
        |
        v
Similarity Search (top-k)
        |
        v
Reranking (CrossEncoder)
        |
        v
Context + Chat History
        |
        v
LLM Response (phi / mistral / mistral-nemo)
```

## Tech Stack
- Python
- Streamlit
- LangChain
- FAISS (vector database)
- Ollama (local LLMs)
- Sentence Transformers (reranking)

## Installation
```Bash
git clone https://github.com/your-username/local-knowledge-assistant.git
cd local-knowledge-assistant

conda create -n rag-env python=3.10 -y
conda activate rag-env

pip install -r requirements.txt
```

## Setup Models
```Bash
ollama pull phi
ollama pull mistral
ollama pull mistral-nemo
ollama pull nomic-embed-text
```
## Run the Application

```Bash
streamlit run app.py
```
## Notes

- The vector store is tied to the embedding model (nomic-embed-text)
- Switching LLMs does not require rebuilding the knowledge base
- Rebuild only if embedding model changes

## Limitations
- No OCR support for scanned PDFs
- No metadata filtering or advanced search
- No evaluation metrics or feedback loop (planned)

## Future Improvements
- Feedback-based learning system
- Answer evaluation metrics
- Improved chunking and document parsing
- UI enhancements
- Deployment support

## Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings and semantic search
- Local LLM integration
- Multi-document processing
- Reranking for improved retrieval quality
- State management and chat memory
- Debugging and system iteration

## License

MIT License
