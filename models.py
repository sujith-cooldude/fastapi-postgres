from sqlalchemy import Integer, Column, Boolean, ForeignKey, String
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)

class Choices(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String)
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey("questions.id"))