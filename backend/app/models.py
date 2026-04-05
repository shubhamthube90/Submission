from sqlalchemy import Column, Integer, String, Text, Boolean
from .database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    status = Column(String, default="queued")
    result = Column(Text, nullable=True)
    is_finalized = Column(Boolean, default=False)
