from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config import get_db
from src.routes import get_current_user
from src.controllers import CategoryController

category = APIRouter()
controller = CategoryController()

@category.get("/", status_code=200)
def getAllCategories(db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return controller.getAllCategories(db)