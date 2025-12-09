from src.schemas import AuditCreate
from src.repositories import AuditRepository
from fastapi import HTTPException
from src.config import engine
from sqlalchemy.orm import Session
from datetime import date
from typing import Union
from fastapi.responses import JSONResponse
from http import HTTPStatus

class AuditController:
    def __init__(self):
        self.audit_repository = AuditRepository()
        
    def create_audits(self, audit: AuditCreate, db: Session):
        try:
            result = self.audit_repository.create(audit, db)
            if result is None:
                raise HTTPException(status_code=400, detail="Audit already exists for this store and date")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    def getAudits(self, auditDate: date, storeId: int | None, db: Session):
        try:
            result = self.audit_repository.getAudits(auditDate, storeId, db)
            if result is None:
                raise HTTPException(status_code=404, detail="A")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def getAuditById(self, id: int, db: Session):
        try:
            result = self.audit_repository.getAuditByID(id, db)
            if not result:
                raise HTTPException(status_code=404, detail="Id Not Found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    def deleteAuditById(self, id: int, db: Session):
        try:
            self.audit_repository.deleteAuditByID(id, db)
            return JSONResponse(
                content={"message": "Auditoria borrada correctamente"},
                status_code=HTTPStatus.OK
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def getAuditDates(self, storeId: int , db: Session):
        try:
            result = self.audit_repository.getAuditDates(storeId, db)
            
            if not result:
                raise HTTPException(status_code=404, detail="Id Not Found ----")    
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

