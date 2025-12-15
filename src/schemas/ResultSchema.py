from pydantic import BaseModel

class ResultBase(BaseModel):
    auditId: int
    quesId: int
    answer: str
    pointsDeducted: str
    state: int | None = 1
    observations: str
    photoPath: str | None = None

class ResultCreate(ResultBase):
    pass

class ResultResponse(ResultBase):
    id: int

    class Config:
        from_attributes = True