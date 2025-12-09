from src.repositories import UserRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from src.schemas import StoreCreate, StoreResponse
from src.repositories import StoreRepository

class StoreController:
    def __init__(self):
        self.storeRepo = StoreRepository()


    def create_Store(self, store: StoreCreate, db: Session):
        try:
            result = self.storeRepo.create(store, db)
            if result is None:
                raise HTTPException(status_code=400, detail="Store already exists")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def getstores(self, db: Session):
        try:
            return self.storeRepo.getStores(db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
