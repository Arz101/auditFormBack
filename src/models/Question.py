from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from .base import Base

class Question(Base):
    __tablename__ = 'Question'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('Category.id'), nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False)
