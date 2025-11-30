from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship

class Vocabulary(Base):
    __tablename__ = "vocabularies"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("vocabulary_categories.id", ondelete="CASCADE"), nullable=True)
    category = relationship("VocabularyCategory", back_populates="vocabularies", uselist=False)
    details = relationship("VocabularyDetails", back_populates="vocabulary", uselist=False)
    examples = relationship("VocabularyExample", back_populates="vocabulary", uselist=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))