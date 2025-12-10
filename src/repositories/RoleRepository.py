from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Role
from src.schemas import RoleResponse


class RoleRepository:
    def __init__(self):
        pass

    def getAllRoles(self, db: Session):
        try:
            query = select(Role.id, Role.role_name.label('name'), Role.description, Role.state).where(Role.state == 1)
            result = db.execute(query).mappings().all()
            return [RoleResponse.model_validate(d) for d in result]
        except Exception as e:
            raise e