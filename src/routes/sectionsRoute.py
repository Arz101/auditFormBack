from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config import get_db
from src.routes import get_current_user
from src.controllers import SectionController
from src.schemas import SectionResponse, SectionCreate

sections = APIRouter()
section_controller = SectionController()

@sections.get("/", response_model=list[SectionResponse],status_code=200)
def getAllSections(db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return section_controller.getSections(db)