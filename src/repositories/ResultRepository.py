from src.schemas import ResultResponse, ResultCreate
from sqlalchemy import select, and_, delete
from src.models import Result
from sqlalchemy.orm import Session, selectinload
from datetime import date

class ResultRepository:
    def __init__(self):
        pass

    def getAllResults(self, db: Session):
        try:
            query = select(Result).where(Result.state == 1)
            result = db.execute(query).scalars().all()

            if result:
                return result
        except Exception as e:
            raise e
        
    def getResultsByAuditID(self, audit_id: int, db: Session):
        try:
            query = select(Result).where(Result.auditId == audit_id)
            result = db.execute(query).scalar_one_or_none()
            if result:
                return result
        except Exception as e:
            raise e