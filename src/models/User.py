from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from .base import Base

class User(Base):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    passwordHash: Mapped[str] = mapped_column(String(120), nullable=False)
    roleId: Mapped[int] = mapped_column(Integer, ForeignKey('Role.id'), nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False)

    UniqueConstraint(email, name='UQ_email')