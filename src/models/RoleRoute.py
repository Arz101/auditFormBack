from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .base import Base

class RoleRoute(Base):
    __tablename__ = 'RoleRoute'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    roleId: Mapped[int] = mapped_column(Integer, nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    method: Mapped[str] = mapped_column(String(10), nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
