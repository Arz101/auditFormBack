from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from .base import Base

class Role(Base):
    __tablename__ = 'Role'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False)

    user = relationship('User', back_populates="role")