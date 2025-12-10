from fastapi import APIRouter, Depends
from src.schemas import QuestionCreate, QuestionResponse, QuestionUpdate
from src.config import get_db
from sqlalchemy.orm import Session
from src.routes import get_current_user
from src.controllers import QuestController
from src.models import User

quest = APIRouter()

quest_controller = QuestController()

@quest.get('/', response_model=list[QuestionResponse], status_code=200)
def getAllQuestions(db: Session = Depends(get_db), userRol: User = Depends(get_current_user)):
    return quest_controller.getAllQuest(db, userRol.roleId)

@quest.get('/{id}', response_model=QuestionResponse)
def getQuestionByID(id: int, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return quest_controller.getQuestionByID(id, db)

@quest.post('/', status_code=201)
def createQuestion(payload: QuestionCreate, db: Session = Depends(get_db), userRol: User = Depends(get_current_user)):
    return quest_controller.createQuestion(payload, db, userRol.roleId)

@quest.put('/{id}', status_code=200)
def updateQuestion(id: int, payload: QuestionUpdate, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    pass

@quest.delete('/{id}', status_code=200)
def deleteQuestionByID(id: int, db: Session = Depends(get_db), userRol: User = Depends(get_current_user)):
    return quest_controller.deleteQuestion(id, db, userRol.roleId)

