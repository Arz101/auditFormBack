from src.schemas import StoreCreate, StoreResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Store

class StoreRepository:
    def __init__(self):
        pass
        
    def create(self, store: StoreCreate, db: Session):
        try:
            new_store = Store(**store.model_dump())
            db.add(new_store)
            db.commit()
            db.refresh(new_store)
            return new_store
        except Exception as e:
            db.rollback()
            raise e
        
    def getStores(self, db: Session):
        try:
            query = select(Store).where(Store.state == 1)
            result = db.execute(query).scalars().all()

            if result: return result
            return None
        except Exception as e:
            raise e