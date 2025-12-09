from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, UniqueConstraint
from .base import Base

class Store(Base):
    __tablename__ = 'Store'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    storeNumber: Mapped[str] = mapped_column(String(120), nullable=False)
    address: Mapped[str] = mapped_column(String(120), nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False)

    UniqueConstraint(storeNumber,name='UQ_storeNumber')

    audits = relationship("Audit", back_populates="store")
