from pydantic import BaseModel


class StoreBase(BaseModel):
    name: str
    storeNumber: str
    address: str
    state: int

class StoreCreate(StoreBase):
    pass

class StoreResponse(StoreBase):
    id: int
    class Config:
        from_attributes = True
    
class StoreUpdate(BaseModel):
    name: str | None
    storeNumber: str | None
    address: str | None
    state: int | None