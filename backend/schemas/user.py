from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, Date
from models.user import UserRole

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class UserCreate(BaseModel):
    telegram_id: str
    name: str
    role: UserRole = UserRole.USER
    info: Optional[dict] = None
    birth_date: Optional[Date] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[Gender] = None
    email: Optional[EmailStr] = None
class UserOut(BaseModel):
    id: int
    telegram_id: str
    name: str
    role: UserRole = UserRole.USER
    info: Optional[dict] = None
    birth_date: Optional[Date] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[Gender] = None
    email: Optional[EmailStr] = None
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }