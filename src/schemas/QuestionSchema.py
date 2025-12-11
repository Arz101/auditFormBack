from pydantic import BaseModel

class QuestionBase(BaseModel):
    text: str
    categoryId: int
    state: int

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    
    class Config:
        from_attributes = True

class QuestionUpdate(BaseModel):
    text: str | None
    categoryId: int | None
    state: int | None