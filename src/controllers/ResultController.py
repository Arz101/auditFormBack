from src.schemas import ResultCreate, ResultResponse
from src.repositories import ResultRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

class ResultController:
    def __init__(self):
        self.repo = ResultRepository()

    def getAll(self, db: Session):
        try:
            result = self.repo.getAllResults(db)
            if result:
                return [ResultResponse.model_validate(c) for c in result]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def getResultByAuditID(self, auditID: int, db: Session):
        try:
            result = self.repo.getResultsByAuditID(auditID,db)
            if result:
                return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))