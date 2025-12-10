from pydantic import BaseModel

class QuestionBase(BaseModel):
    text: str
    category_id: int
    state: int

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    
    class Config:
        from_attributes = True

class QuestionUpdate(BaseModel):
    text: str | None
    category_id: int | None
    state: int | None