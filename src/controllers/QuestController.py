from sqlalchemy.orm import Session
from src.models import User
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.repositories import QuestRepository
from src.schemas import QuestionCreate
from http import HTTPStatus


class QuestController:
    def __init__(self):
        self.questRepo = QuestRepository()

    def getAllQuest(self, db: Session, userRol: int):
        if userRol != 1:
            raise HTTPException(status_code=401, detail="Admin")
        try:
            return self.questRepo.getAllQuestions(db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def getQuestionByID(self, id: int, db: Session):
        try:
            return self.questRepo.getQuestionByID(id, db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def createQuestion(self, quest: QuestionCreate, db: Session, userRol: int):
        if userRol != 1:
            raise HTTPException(status_code=401, detail="Admin")
        try:
            return self.questRepo.create(quest, db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def deleteQuestion(self, id: int, db: Session, userRol: int):
        if userRol != 1:
            raise HTTPException(status_code=401, detail="Admin")
        try:
            if self.questRepo.delete(id, db) == 1:
                return JSONResponse(
                    content={"message" : "Pregunta borrada correctamente"},
                    status_code=HTTPStatus.OK
                )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

