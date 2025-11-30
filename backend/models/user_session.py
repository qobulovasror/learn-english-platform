from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="user_sessions")
    refresh_token_hash = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    device_name = Column(String, nullable=False)
    device_ip = Column(String, nullable=False)
    is_revoked = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))
    expires_at = Column(DateTime, nullable=False)