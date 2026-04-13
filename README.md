````markdown
# RAG Document Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

A local Retrieval-Augmented Generation (RAG) chatbot that enables users to upload documents and query their contents. The system retrieves relevant context using vector search and generates grounded responses using a local LLM.

## Features

- Document ingestion and processing (.txt)
- Semantic search using FAISS
- Context-aware response generation
- Fully local execution (no API dependency)
- Streamlit-based interface

## Architecture

```text
Upload Document
      |
      v
Text Chunking
      |
      v
Embeddings (Ollama)
      |
      v
Vector Store (FAISS)
      |
      v
User Query
      |
      v
Similarity Search
      |
      v
Context Injection
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

## Project Structure

```
rag-document-chatbot/
├── app.py
├── requirements.txt
├── README.md
```

## Installation

```bash
git clone https://github.com/your-username/rag-document-chatbot.git
cd rag-document-chatbot

conda create -n rag-env python=3.10 -y
conda activate rag-env

pip install -r requirements.txt
```

## Running the Application

Ensure Ollama is installed and running:

```bash
ollama run phi
```

Start the app:

```bash
streamlit run app.py
```

## Current Limitations

* Session-based storage (no persistence)
* Text files only
* No chat memory
* No source attribution

## Roadmap

* Persistent vector database
* PDF and multi-file support
* Chat history and memory
* Source citations
* UI improvements

## Learning Outcomes

* RAG pipeline design
* Vector embeddings and similarity search
* Local LLM integration
* End-to-end AI application development

## License

MIT License



