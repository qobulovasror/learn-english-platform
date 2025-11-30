from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship

class VocabularyExample(Base):
    __tablename__ = "vocabulary_examples"

    id = Column(Integer, primary_key=True, index=True)
    vocabulary_id = Column(Integer, ForeignKey("vocabularies.id"), nullable=False)
    vocabulary = relationship("Vocabulary", back_populates="examples")
    example_text = Column(String, nullable=False)
    translation = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))