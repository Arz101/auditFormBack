from src.models import Category
from sqlalchemy import select
from sqlalchemy.orm import Session

class CategoryRepository:
    def __init__(self):
        pass

    def getAllCategories(self, db: Session):
        try:
            query = select(Category).where(Category.state == 1)
            result = db.execute(query).scalars().all()

            if result:
                return result
        except Exception as e:
            raise e