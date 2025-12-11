from fastapi import APIRouter
from src.schemas import AuditCreate, AuditResponse, AuditResponseDate, AuditUpdate
from src.controllers import AuditController
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from src.config import get_db
from datetime import date
from typing import Optional, Union
from .authRoutes import get_current_user

audit = APIRouter()
audit_controller = AuditController()


@audit.post("/", response_model=AuditResponse, status_code=201)
def createAudit(audit_obj: AuditCreate, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return audit_controller.create_audits(audit_obj, db)

@audit.get("/", response_model=list[AuditResponse], status_code=200)
def getAudits(storeId: Optional[int], date: date, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return audit_controller.getAudits(date, storeId, db)

@audit.get("/{id}", response_model=AuditResponse, status_code=200)
def getAuditByID(id: int, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return audit_controller.getAuditById(id, db)

@audit.delete("/{id}", response_model=AuditResponse, status_code=200)
def deleteAuditByID(id: int, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return audit_controller.deleteAuditById(id, db)

@audit.get("/dates/", response_model=list[AuditResponseDate], status_code=200)
def getAuditDates(storeId: int, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return audit_controller.getAuditDates(storeId, db)

@audit.put("/{id}")
def updateAudit(id: int, payload: AuditUpdate, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    pass
