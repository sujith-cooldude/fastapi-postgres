from fastapi import FastAPI, Depends, HTTPException
from typing import List, Annotated
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from sqlalchemy.orm import session

app = FastAPI()

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[session, Depends(get_db)]

@app.post("/questions/")
async def create_question(question: QuestionBase, db: db_dependency):
    db_question = models.Question(question_text = question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choices = models.Choices(choice_text= choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choices)
    db.commit()
    
