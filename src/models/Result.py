from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from .base import Base

class Result(Base):
    __tablename__ = 'Result'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    auditId: Mapped[int] = mapped_column(Integer, ForeignKey('Audit.id'),nullable=False)
    questId: Mapped[int] = mapped_column(Integer, ForeignKey('Question.id'),nullable=False)
    answer: Mapped[str] = mapped_column(String(255), nullable=True)
    pointsDeducted: Mapped[int] = mapped_column(Integer, nullable=False)
    state: Mapped[int] = mapped_column(Integer, nullable=False)
    observations: Mapped[str | None] = mapped_column(String, nullable=True)
    photoPath: Mapped[str | None] = mapped_column(String, nullable=True)