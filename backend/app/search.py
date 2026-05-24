from sqlalchemy import text
from app.database import SessionLocal
from app.embeddings import generate_embedding
from app.models import DocumentChunk


def search_documents(query, limit=4):

    db = SessionLocal()

    try:

        embedding = generate_embedding(query)

        sql = text("""
            SELECT
                document_name,
                page_number,
                chunk_text,
                embedding <-> :embedding AS distance
            FROM document_chunks
            ORDER BY embedding <-> :embedding
            LIMIT :limit
        """)

        results = db.execute(
            sql,
            {
                "embedding": str(embedding),
                "limit": limit
            }
        )

        return results.fetchall()

    finally:
        db.close()