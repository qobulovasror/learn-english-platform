from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VocabularyCreate(BaseModel):
    word: str
    translation: str
    category_id: Optional[int] = None

class VocabularyOut(BaseModel):
    id: int
    word: str
    translation: str
    category_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True