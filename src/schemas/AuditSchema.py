from pydantic import BaseModel, field_validator, model_validator
from datetime import date
from .StoreSchema import StoreResponse

class AuditBase(BaseModel):
    user_id: int
    store_id: int
    contact_name: str | None = None
    audit_date: date
    start_time: str | None = None
    end_time: str | None = None
    initial_score: int
    final_score: int | None = None
    observations: str | None = None
    state: int

class AuditCreate(AuditBase):
    pass

class AuditUpdate(BaseModel):
    contact_name: str | None = None
    start_time: str | None = None
    end_time: str | None = None
    initial_score: int | None = None
    final_score: int | None = None
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
    audit_date: date

    class Config:
        from_attributes = True 