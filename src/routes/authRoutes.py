from typing import Annotated
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.controllers import UserController
from src.config import get_db
from src.schemas import UserAccess, LoginResponse
from jwt.exceptions import InvalidTokenError
import jwt
from pydantic import BaseModel
from src.models import User

auth = APIRouter()
user_controller = UserController()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class Token(BaseModel):
    access_token: str
    token_type: str


@auth.post("/login", response_model=LoginResponse)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user: LoginResponse = user_controller.verifyUser(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=user_controller.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_controller.create_access_token(
        data={"sub" : str(user.id)}, expires_delta=access_token_expires
    )
    user_with_toke = user.model_copy(update={"token":access_token, "access_token" : access_token})
    return user_with_toke

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate Credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, user_controller.SECRET_KEY, algorithms=[user_controller.ALGORITHM])
        user_data = payload.get("sub")
        
        if user_data is None:
            raise credentials_exception
        token_data = int(user_data)
    except InvalidTokenError:
        raise credentials_exception
    
    user = user_controller.get_user(token_data, db)

    if user is None:
        raise credentials_exception
    return user