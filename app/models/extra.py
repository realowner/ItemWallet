from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from app.models.mixins import TimestampMixin
from app.db.base import Base


class Game(TimestampMixin, Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    item_types: Mapped[list["ItemType"]] = relationship(back_populates="game", cascade="all, delete-orphan")


class ItemType(TimestampMixin, Base):
    __tablename__ = "item_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False)
    game: Mapped["Game"] = relationship(back_populates="item_types")
