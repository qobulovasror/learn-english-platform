from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship

class VocabularyCategory(Base):
    __tablename__ = "vocabulary_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    vocabularies = relationship("Vocabulary", back_populates="category")