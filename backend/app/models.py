from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

from pgvector.sqlalchemy import Vector

Base = declarative_base()

class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True)

    document_name = Column(Text)

    page_number = Column(Integer)

    chunk_text = Column(Text)

    embedding = Column(Vector(384))