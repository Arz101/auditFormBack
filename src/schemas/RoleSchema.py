from pydantic import BaseModel


class RoleBase(BaseModel):
    role_name: str
    description: str | None = None
    state: int

class RoleCreate(RoleBase):
    pass


class RoleResponse(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True
