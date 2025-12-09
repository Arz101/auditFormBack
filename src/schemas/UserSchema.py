from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    passwordHash: str
    roleId: int
    state: int

class UserCreate(UserBase):
    pass

class Login(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserAccess:
    id: int
    email: str
    roleId: int
    stateL: int

class UserUpdate(BaseModel):
    name: str | None
    state: str | None
    roleId: int | None