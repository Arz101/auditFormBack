from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config import get_db
from src.routes import get_current_user
from src.repositories import RoleRepository
from src.schemas import RoleResponse, RoleCreate
from http import HTTPStatus

roles = APIRouter()

role = RoleRepository()

@roles.get('/',response_model=list[RoleResponse], status_code=201)
def getAllRoles(db: Session = Depends(get_db), _ = Depends(get_current_user)):
    try:
        return role.getAllRoles(db)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
    