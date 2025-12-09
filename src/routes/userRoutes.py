from fastapi import APIRouter, Depends
from src.config import get_db
from src.controllers import UserController
from src.schemas import UserCreate, UserResponse
from sqlalchemy.orm import Session
from .authRoutes import get_current_user

user = APIRouter()

user_controller = UserController()

@user.post("/", response_model=UserResponse, status_code=201)
def createUser(payload: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(payload, db)

@user.get("/", response_model=list[UserResponse], status_code=200)
def getUsers(db: Session = Depends(get_db), rol = Depends(get_current_user)):
    return user_controller.get_user(db, rol)