from fastapi import FastAPI
from pydantic import BaseModel

from app.search import search_documents
from fastapi.middleware.cors import CORSMiddleware

from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

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

    response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

    return {
        "answer": response.choices[0].message.content
    }