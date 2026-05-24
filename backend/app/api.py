from fastapi import FastAPI
from pydantic import BaseModel

from app.search import search_documents
from fastapi.middleware.cors import CORSMiddleware

import ollama

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")

def home():
    return {"message": "Enterprise RAG API Running"}

@app.post("/chat")
def chat(request: ChatRequest):

    results = search_documents(request.question)

    context = "\n\n".join([
        result.chunk_text[:300]
        for result in results[:2]
    ])

    prompt = f"""
You are an enterprise AI assistant.

Answer briefly using ONLY the context below.

If the answer is missing, say:
"I could not find the answer in the documents."

CONTEXT:
{context}

QUESTION:
{request.question}

ANSWER:
"""

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "answer": response["message"]["content"]
    }