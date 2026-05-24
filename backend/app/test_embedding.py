from embeddings import generate_embedding

text = "Attention mechanisms in transformers"

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])