from src.models import Section
from sqlalchemy.orm import Session
from sqlalchemy import select

class SectionRepository:
    def __init__(self):
        pass

    def getAllSections(self, db: Session):
        try:
            query = select(Section).where(Section.state == 1)
            result = db.execute(query).scalars().all()

            if result:
                return result
        except Exception as e:
            raise e