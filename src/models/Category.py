from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Text, func
from sqlalchemy.dialects.mssql import DATETIMEOFFSET
from datetime import datetime
from .base import Base

class Category(Base):
    __tablename__ = 'Category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    weight: Mapped[int] = mapped_column(Integer, nullable=False)
    sectionId: Mapped[int] = mapped_column(Integer, nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    createdAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset())
    updatedAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset(), onupdate=func.sysdatetimeoffset())
