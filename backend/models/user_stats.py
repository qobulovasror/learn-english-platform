from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class UserStats(Base):
    __tablename__ = "user_stats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="user_stats")
    xp = Column(Integer, nullable=False, default=0)
    level = Column(Integer, nullable=False, default=0)
    streak = Column(Integer, nullable=False, default=0)
    badges = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))