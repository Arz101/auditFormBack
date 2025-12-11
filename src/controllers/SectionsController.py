from src.schemas import SectionCreate, SectionResponse
from sqlalchemy.orm import Session 
from fastapi import HTTPException
from src.repositories import SectionRepository

class SectionController:
    def __init__(self):
        self.section_repo = SectionRepository()

    def getSections(self, db: Session):
        try:
            result = self.section_repo.getAllSections(db)
            if result:
                return [SectionResponse.model_validate(d) for d in result]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
