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


class VocabularyCategoryCreate(BaseModel):
    name: str

class VocabularyCategoryOut(BaseModel):
    id: int
    name: str
    created_at: datetime
    vocabularies: list[VocabularyOut]
    class Config:
        from_attributes = True
class VocabularyDetailsCreate(BaseModel):
    vocabulary_id: int
    details: str

class VocabularyDetailsOut(BaseModel):
    id: int
    vocabulary_id: int
    details: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True