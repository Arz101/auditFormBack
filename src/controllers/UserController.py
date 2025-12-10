from src.repositories import UserRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from pwdlib import PasswordHash
from src.schemas import UserResponse, UserAccess, UserCreate
from src.models import User
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import os
import jwt

load_dotenv()


class UserController:
    def __init__(self):
        self.userRepo = UserRepository()
        self.passwordHash = PasswordHash.recommended()
        self.ALGORITHM = os.getenv('ALGORITHM')
        self.SECRET_KEY= os.getenv('SECRET_KEY')
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

    def verifyUser(self, email: str, password: str, db: Session):
        try:
            user = self.userRepo.verifyUser(email, db)
            if user:
                if self.verify_password(user, password):
                    return UserAccess(
                        id=user.id,
                        email=user.email,
                        roleId=user.roleId,
                        state=user.state
                    )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def verify_password(self, user: UserResponse, password: str):
        return self.passwordHash.verify(password, user.passwordHash)
    
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    def get_user(self, userId: int, db: Session):
        try:
            return self.userRepo.getUserByID(userId, db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def hash_password(self, plain_password):
        return self.passwordHash.hash(plain_password)

    def create_user(self, user: UserCreate, db: Session):
        user = user.model_copy(update={"passwordHash" : self.hash_password(user.passwordHash)})
        try:
            result = self.userRepo.create(user, db)
            if not result:
                raise HTTPException(status_code=400, detail="User already exists")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def getUsers(self, db: Session, user: User):
        if user.roleId != 1:
            raise HTTPException(status_code=401, detail="No Authentication")
        
        try:
            result = self.userRepo.getUsers(db)
            if result is None:
                raise HTTPException(status_code=404, detail="Empty")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



