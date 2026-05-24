from pypdf import PdfReader
from pathlib import Path

from app.chunking import chunk_text
from app.embeddings import generate_embedding

from app.database import SessionLocal
from app.models import DocumentChunk

PDF_FOLDER = Path("../data/pdfs")

db = SessionLocal()

for pdf_file in PDF_FOLDER.glob("*.pdf"):

    print(f"\nReading: {pdf_file.name}")

    reader = PdfReader(pdf_file)

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:
            text = text.replace("\x00", " ")

        if not text:
            continue

        chunks = chunk_text(text)

        print(f"Generated {len(chunks)} chunks")

        for chunk in chunks:

            embedding = generate_embedding(chunk)

            document_chunk = DocumentChunk(
                document_name=pdf_file.name,
                page_number=page_number + 1,
                chunk_text=chunk,
                embedding=embedding
            )

            db.add(document_chunk)

db.commit()

print("\nAll chunks stored successfully")