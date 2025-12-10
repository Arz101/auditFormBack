from pydantic import BaseModel, field_validator
from .RoleSchema import RoleResponse

class UserBase(BaseModel):
    email: str
    name: str
    passwordHash: str
    roleId: int
    state: int | None = 1
    @field_validator("roleId", "state", mode="before")
    def convert_to_int(cls, v):
        if isinstance(v, str) and v.isdigit():
            return int(v)
        return v


class UserCreate(UserBase):
    pass

class Login(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True

class UserAccess(BaseModel):
    id: int
    email: str
    roleId: int
    state: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: str | None
    state: str | None
    roleId: int | None

class LoginResponse(BaseModel):
    access_token: str | None = None
    id: int
    name: str
    email: str
    roleId: int
    role_name: str
    token: str | None = None

    class Config:
        from_attributes = True


class UserWithRole(BaseModel):
    id: int
    name: str
    email: str
    role: RoleResponse | None = None
    state: int
    class Config:
        from_attributes = True