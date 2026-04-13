# RAG Document Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# RAG Document Chatbot

A local AI-powered chatbot that lets users upload documents and ask questions based on their contents. The app uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant context from uploaded files and generate grounded answers with a local language model.

## Overview

This project was built to explore how modern AI applications combine document retrieval, vector search, and large language models into a usable end-to-end system. It provides a simple interface for uploading documents, indexing them, and querying them through a chatbot workflow.

## Features

- Upload and process text-based documents
- Convert document content into vector embeddings
- Store embeddings in a FAISS vector database
- Retrieve relevant chunks using similarity search
- Generate context-aware responses with Ollama
- Run fully locally without paid API usage
- Simple user interface built with Streamlit

## Architecture Flow

```text
User uploads document
        |
        v
Document loader
        |
        v
Text chunking
        |
        v
Embedding generation
        |
        v
FAISS vector store
        |
        v
User enters question
        |
        v
Similarity search retrieves relevant chunks
        |
        v
Context is passed to the local LLM
        |
        v
Response is generated and shown in the UI
```
##How It Works

When a user uploads a document, the file is loaded and split into smaller chunks. Each chunk is converted into an embedding and stored in a FAISS vector database. When the user asks a question, the system performs a similarity search to retrieve the most relevant chunks. Those chunks are then passed as context to the local language model, which generates an answer grounded in the uploaded document.

##Tech Stack

Python
Streamlit
LangChain
FAISS
Ollama

## Project Structure

```
rag-document-chatbot/
│
├── app.py
├── README.md
├── requirements.txt
└── sample_data/
```


## Installation

Clone the repository:

```
git clone https://github.com/your-username/rag-document-chatbot.git
cd rag-document-chatbot
```

Create and activate a virtual environment:
```
conda create -n rag-env python=3.10 -y
conda activate rag-env
```
Install dependencies:
```
pip install -r requirements.txt
Running the Project
```
First, make sure Ollama is installed and running locally.

Pull and run a lightweight model:
```
ollama run phi
```
Then start the Streamlit application:
```
streamlit run app.py
Example Use Cases
Personal knowledge assistant
Study and revision chatbot
Internal documentation assistant
Notes and report Q&A tool
Domain-specific local chatbot
```
## Learning Outcomes

This project demonstrates understanding of:

Retrieval-Augmented Generation (RAG)
Vector embeddings and semantic search
Local LLM integration
Streamlit app development
End-to-end AI application workflow
Debugging package, environment, and model issues

## Roadmap
Current
Document upload
Vector search with FAISS
Local LLM response generation
Streamlit user interface

## Planned Improvements

PDF support
Multiple file uploads
Better chunking strategy
Chat history and memory
Source citations in responses
Improved UI styling
Deployment support

## Why This Project Matters

This project goes beyond a basic chatbot by combining retrieval and generation into a system that answers questions using custom user-provided data. It reflects intermediate-level understanding of how practical AI applications are structured and deployed.

License

This project is licensed under the MIT License.
