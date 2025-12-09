from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date
from datetime import date
from .base import Base

class Audit(Base):
    __tablename__ = 'Audit'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('User.id'), nullable=False)
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey('Store.id'), nullable=False)
    contact_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    audit_date: Mapped[date] = mapped_column(Date, nullable=False)
    start_time: Mapped[str | None] = mapped_column(String(10), nullable=True)
    end_time: Mapped[str | None] = mapped_column(String(10), nullable=True)
    initial_score: Mapped[int] = mapped_column(Integer, nullable=False)
    final_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    observations: Mapped[str | None] = mapped_column(String, nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False)

    store = relationship("Store", back_populates="audits")