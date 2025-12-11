from src.repositories import CategoryRepository
from src.config import get_db
from sqlalchemy import select, and_, delete
from src.models import User, Role
from fastapi import HTTPException
from sqlalchemy.orm import Session, selectinload
from src.schemas import CategoryResponse, CategoryCreate 

class CategoryController:
    def __init__(self):
        self.repo = CategoryRepository()

    def getAllCategories(self, db: Session):
        try:
            result = self.repo.getAllCategories(db)
            if result:
                return [CategoryResponse.model_validate(c) for c in result]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))