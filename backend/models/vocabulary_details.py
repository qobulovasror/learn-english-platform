from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base
from sqlalchemy.orm import relationship
from enum import Enum

class PartOfSpeech(str, Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    PRONOUN = "pronoun"
    INTERJECTION = "interjection"

class Level(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

class VocabularyDetails(Base):
    __tablename__ = "vocabulary_details"

    id = Column(Integer, primary_key=True, index=True)
    vocabulary_id = Column(Integer, ForeignKey("vocabularies.id"), nullable=False, unique=True)
    vocabulary = relationship("Vocabulary", back_populates="details")
    definition = Column(String, nullable=True)
    synonyms_ids = Column(JSONB, nullable=True)
    antonyms_ids = Column(JSONB, nullable=True)
    ipa = Column(String, nullable=True)
    audio_url = Column(String, nullable=True)
    level = Column(SQLAlchemyEnum(Level), nullable=True)
    part_of_speech = Column(SQLAlchemyEnum(PartOfSpeech), nullable=True)