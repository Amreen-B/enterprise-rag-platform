# Enterprise RAG Architecture

```text
                ┌─────────────────────┐
                │     Next.js UI      │
                │   Frontend Client   │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │     FastAPI API     │
                │    Backend Server   │
                └─────────┬───────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼

┌───────────────────┐         ┌───────────────────┐
│ Embedding Model   │         │     Ollama LLM    │
│ SentenceTransform │         │       phi3        │
└─────────┬─────────┘         └───────────────────┘
          │
          ▼

┌─────────────────────────────┐
│ PostgreSQL + pgvector DB    │
│ Vector Similarity Search    │
└─────────────────────────────┘
```

## Flow

1. User asks question from frontend
2. FastAPI receives request
3. Embedding model converts query to vectors
4. pgvector performs semantic similarity search
5. Relevant chunks retrieved
6. Context sent to Ollama LLM
7. Final answer returned to frontend