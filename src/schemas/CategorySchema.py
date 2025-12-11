from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: str | None = None
    weight: int
    sectionId: int
    state: int

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True
