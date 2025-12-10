from src.schemas import UserCreate, UserResponse, LoginResponse, UserWithRole, RoleResponse
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
            query = (
                select(User)
                .where(User.email == email)
            )
            result = db.execute(query).scalar_one_or_none()

            if result:
                return result
            return None
        except Exception as e:
            raise e
        
    def getUserByID(self, id: int, db: Session):
        try:
            query = (
                select(User.id, User.name, User.email, Role.id.label("roleId"), Role.role_name)
                .join(Role, Role.id == User.roleId)
                .where(User.id == id)
            )
            result = db.execute(query).mappings().one_or_none()
            if result:
                return LoginResponse.model_validate(result)
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
            #query = (
             #   select(User.id, User.name, User.email, Role.id.label("roleId"), Role.role_name)
             #   .join(Role, Role.id == User.roleId)
             #   .where(User.state == 1)
            #)

            query = select(User).where(User.state == 1)
            
            users = db.execute(query).scalars().all()


            result = []

            for user in users:
                role_query = (
                    select(Role.id, Role.role_name.label("name"))
                    .where(Role.id == user.roleId)
                )

                role_row = db.execute(role_query).mappings().one_or_none()

                role_response = RoleResponse.model_validate(role_row) if role_row else None

                user_with_role = UserWithRole(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    role=role_response,
                    state=user.state
                )

                result.append(user_with_role)

            return result
        except Exception as e:
            raise e
        