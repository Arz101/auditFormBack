from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, func
from sqlalchemy.dialects.mssql import DATETIMEOFFSET
from datetime import datetime
from .base import Base

class Question(Base):
    __tablename__ = 'Question'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    categoryId: Mapped[int] = mapped_column(Integer, ForeignKey('Category.id'), nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset())
    updatedAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset(), onupdate=func.sysdatetimeoffset())