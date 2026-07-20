from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Memory(BaseModel):
    """
    Representa uma memória permanente do Jarvis.
    """

    __tablename__ = "memories"

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    memory_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    importance: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False,
    )
