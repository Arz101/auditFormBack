from src.schemas import UserCreate
from src.config import get_db
from sqlalchemy import select, and_, delete
from src.models import User, Role
from fastapi import Depends
from sqlalchemy.orm import Session, selectinload
from datetime import date

class UserRepository:
    def __init__(self):
        pass

    def verifyUser(self, email: str, db: Session):
        try:
            query = select(User).where(User.email == email)
            result = db.execute(query).scalar_one_or_none()

            if result:
                return result
            return None
        except Exception as e:
            raise e
        
    def getUserByID(self, id: int, db: Session):
        try:
            query = select(User).where(User.id == id)
            result = db.execute(query).scalar_one_or_none()
            if result:
                return result
            return None
        except Exception as e:
            raise e


    def create(self, user: UserCreate, db: Session):
        try:
            result = select(User).where(User.email == user.email)

            existing_user = db.execute(result).scalar_one_or_none()
            if existing_user:
                return None
            
            new_user = User(**user.model_dump())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except Exception as e:
            db.rollback()
            raise e
    
    def getUsers(self, db: Session):
        try:
            query = select(User).where(User.state == 1)
            result = db.execute(query).scalars().all()
            if result:
                return result
            return None
        except Exception as e:
            raise e
        