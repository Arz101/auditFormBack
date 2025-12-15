from fastapi import APIRouter, Depends
from src.config import get_db
from src.routes import get_current_user
from sqlalchemy.orm import Session
from src.controllers import ResultController
from src.schemas import ResultResponse, ResultCreate

results = APIRouter()
controller = ResultController()

@results.get("/",  response_model=list[ResultResponse], status_code=200)
def getAllResults(db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return controller.getAll(db)

@results.get('/{id}')
def getResultByID(id: int, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return controller.getResultByAuditID(id, db)