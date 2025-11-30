from sqlalchemy import Column, Integer, DateTime, Float
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="user_progress")
    vocabulary_id = Column(Integer, ForeignKey("vocabularies.id"), nullable=False)
    vocabulary = relationship("Vocabulary", back_populates="user_progress")
    familiarity = Column(Integer, nullable=False, default=0)
    test_correct = Column(Integer, nullable=False, default=0)
    test_wrong = Column(Integer, nullable=False, default=0)
    last_reviewed = Column(DateTime, nullable=True)
    next_review = Column(DateTime, nullable=True)
    interval_days = Column(Integer, nullable=False, default=1)
    ease_factor = Column(Float, nullable=False, default=2.5)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))