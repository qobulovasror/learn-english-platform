from sqlalchemy import Column, Integer, String, DateTime, JSONB, Enum
from models.base import Base
from datetime import datetime, UTC
from sqlalchemy.types import Enum as SQLAlchemyEnum

class UserRole(SQLAlchemyEnum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True, nullable=True)
    name = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.USER)
    info = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))