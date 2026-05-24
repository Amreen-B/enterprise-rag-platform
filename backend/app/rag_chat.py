from app.search import search_documents
import ollama

query = input("Ask a question: ")

results = search_documents(query)

context = "\n\n".join([
    result.chunk_text for result in results
])

prompt = f"""
You are an AI research assistant.

Answer the user's question ONLY using the provided context.

If the answer is not in the context, say:
"I could not find the answer in the documents."

Be detailed and technical when possible.

==============Context==============

{context}

===================================

Question: 
{query}

ANSWER:
"""

print("\n================ CONTEXT ================\n")
print(context[:3000])
print("\n=========================================\n")

response = ollama.chat(
    model="phi3",
    messages = [{
        "role":  "user",
        "content": prompt
    }]
)

print("\n===============================")
print("Answer:")
print("===============================\n")

print(response.message.content)