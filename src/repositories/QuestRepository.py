from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from src.schemas import QuestionResponse, QuestionCreate
from src.models import Question

class QuestRepository:
    def __init__(self):
        pass

    def getAllQuestions(self, db: Session):
        try:
            query = select(Question).where(Question.state == 1)
            result = db.execute(query).scalars().all()

            return result
        except Exception as e:
            raise e
        
    def getQuestionByID(self, id: int, db: Session):
        try:
            query = select(Question).where(Question.id == id)
            result = db.execute(query).scalar_one_or_none()

            return result
        except Exception as e:
            raise e

    def create(self, quest: QuestionCreate, db: Session):
        try:    
            new_question = Question(**quest.model_dump())
            db.add(new_question)
            db.commit()
            db.refresh(new_question)
            return new_question
        except Exception as e:
            raise e
        
    def delete(self, id: int, db: Session):
        try:
            query = delete(Question).where(Question.id == id)
            db.execute(query)
            db.commit()
            return 1
        except Exception as e:
            db.rollback()
            raise e
