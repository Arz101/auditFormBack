from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date, func
from sqlalchemy.dialects.mssql import DATETIMEOFFSET
from datetime import date, datetime
from .base import Base

class Audit(Base):
    __tablename__ = 'Audit'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(Integer, ForeignKey('User.id'), nullable=False)
    storeId: Mapped[int] = mapped_column(Integer, ForeignKey('Store.id'), nullable=False)
    contactName: Mapped[str | None] = mapped_column(String(120), nullable=True)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    startTime: Mapped[str | None] = mapped_column(String(10), nullable=True)
    endTime: Mapped[str | None] = mapped_column(String(10), nullable=True)
    initialScore: Mapped[int] = mapped_column(Integer, nullable=False)
    finalScore: Mapped[int | None] = mapped_column(Integer, nullable=True)
    observations: Mapped[str | None] = mapped_column(String, nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset())
    updatedAt: Mapped[datetime] = mapped_column(DATETIMEOFFSET, nullable=False, server_default=func.sysdatetimeoffset(), onupdate=func.sysdatetimeoffset())

    store = relationship("Store", back_populates="audits")
