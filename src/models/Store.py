from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, UniqueConstraint, func
from sqlalchemy.dialects.mssql import DATETIMEOFFSET
from datetime import datetime
from .base import Base

class Store(Base):
    __tablename__ = 'Store'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    storeNumber: Mapped[str] = mapped_column(String(120), nullable=False)
    address: Mapped[str] = mapped_column(String(120), nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset())
    updatedAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset(), onupdate=func.sysdatetimeoffset())

    UniqueConstraint(storeNumber,name='UQ_storeNumber')

    audits = relationship("Audit", back_populates="store")
