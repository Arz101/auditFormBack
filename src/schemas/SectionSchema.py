from pydantic import BaseModel

class SectionBase(BaseModel):
    name: str
    description: str | None = None
    state: int | None = 1

class SectionCreate(SectionBase):
    pass

class SectionResponse(SectionBase):
    id: int

    class Config:
        from_attributes = True

    