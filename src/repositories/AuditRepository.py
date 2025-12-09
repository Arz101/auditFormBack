from src.schemas import AuditCreate, AuditResponse
from src.config import get_db
from sqlalchemy import select, and_, delete
from src.models import Audit, Store
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from datetime import date

class AuditRepository:
    def __init__(self):
        pass

    def create(self, audit: AuditCreate, db: Session):
        try:
            result = select(Audit).where(and_(Audit.store_id == audit.store_id, Audit.audit_date == audit.audit_date))
            
            existing_audit = db.execute(result).scalar_one_or_none()
            if existing_audit:
                return None  
            
            new_audit = Audit(**audit.model_dump())    
            db.add(new_audit)
            db.commit()
            db.refresh(new_audit)
            return new_audit
        except Exception as e:
            db.rollback()
            raise e
        
    def getAudits(self, auditDate: date, storeId: int | None, db: Session):
        try:
            if storeId:
                query = (
                    select(Audit)
                    .options(selectinload(Audit.store))
                    .where(and_(Audit.audit_date == auditDate, Audit.store_id == storeId))
                )
            else:
                query = (
                    select(Audit)
                    .options(selectinload(Audit.store))
                    .where(Audit.audit_date == auditDate)
                )
            audits = db.execute(query).scalars().all()
            return audits   
        except Exception as e:
            raise e

    def getAuditByID(self, _id: int, db: Session):
        try:
            query = select(Audit).where(Audit.id == _id)
            result = db.execute(query).scalar_one_or_none()

            if result:
                return result
            return None
        except Exception as e:
            raise e
        
    def deleteAuditByID(self, id: int, db: Session):
        try:
            query = delete(Audit).where(Audit.id == id)
            db.execute(query)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        
    def getAuditDates(self, storeId: int, db: Session):
        try:
            query = select(Audit.audit_date).where(Audit.store_id == storeId)
            result = db.execute(query).scalars().all()

            if result:
                return [{"audit_date": d} for d in result]
            return None
        except Exception as e:
            raise e