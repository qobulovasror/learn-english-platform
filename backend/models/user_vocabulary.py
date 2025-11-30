from sqlalchemy import Column, Integer, DateTime, ForeignKey
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship

class UserVocabulary(Base):
    __tablename__ = "user_vocabularies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="user_vocabularies")
    vocabulary_id = Column(Integer, ForeignKey("vocabularies.id"), nullable=False)
    vocabulary = relationship("Vocabulary", back_populates="user_vocabularies")
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))