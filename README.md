# Enterprise RAG AI Platform

Production-grade Retrieval-Augmented Generation (RAG) platform built using:

- FastAPI
- PostgreSQL + pgvector
- Ollama (Local LLMs)
- Sentence Transformers
- Next.js 15
- Docker
- Vector Similarity Search

---

# Features

- Semantic document search
- AI-powered question answering
- Local LLM inference using Ollama
- Vector database retrieval
- Full-stack architecture
- FastAPI backend APIs
- Next.js frontend UI
- Dockerized PostgreSQL with pgvector

---

# Architecture

User Query
↓
FastAPI Backend
↓
Embedding Generation
↓
pgvector Semantic Search
↓
Context Retrieval
↓
Ollama LLM
↓
Final AI Response

---

# Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector

## Frontend
- Next.js
- React
- TailwindCSS

## AI/ML
- Sentence Transformers
- Ollama
- Vector Embeddings

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Amreen-B/enterprise-rag-platform.git
cd enterprise-rag-platform
```

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.api:app --reload
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

# API Endpoint

POST `/chat`

Example Request:

```json
{
  "question": "What is chain of thought prompting?"
}
```

---

# Future Improvements

- JWT Authentication
- Multi-user support
- Cloud deployment
- Streaming responses
- LangChain integration
- Multi-document upload
- Admin dashboard

---

Author: Amreen