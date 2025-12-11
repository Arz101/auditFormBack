from pydantic import BaseModel, field_validator, model_validator
from .StoreSchema import StoreResponse
import datetime

class AuditBase(BaseModel):
    userId: int
    storeId: int
    contactName: str | None = None
    date: datetime.date
    startTime: str | None = None
    endTime: str | None = None
    initialScore: int
    finalScore: int | None = None
    observations: str | None = None
    state: int

class AuditCreate(AuditBase):
    pass

class AuditUpdate(BaseModel):
    contactName: str | None = None
    startTime: str | None = None
    endTime: str | None = None
    initialScore: int | None = None
    finalScore: int | None = None
    observations: str | None = None
    state: int | None = None

    @model_validator(mode='before')
    def check_not_empty(cls, values):
        if not values:
            raise ValueError("At least one field must be provided for update.")
        return values
    
class AuditResponse(AuditBase):
    id: int
    store: StoreResponse | None = None

    class Config:
        from_attributes = True 

class AuditResponseDate(BaseModel):
    date: datetime.date

    class Config:
        from_attributes = True 