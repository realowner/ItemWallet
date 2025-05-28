from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Float

from app.models.mixins import TimestampMixin
from app.db.base import Base


class Game(TimestampMixin, Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)

    item_types: Mapped[list["ItemType"]] = relationship(back_populates="game", cascade="all, delete-orphan")


class ItemType(TimestampMixin, Base):
    __tablename__ = "item_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False)

    game: Mapped["Game"] = relationship(back_populates="item_types")
    type_items: Mapped[list["Item"]] = relationship(back_populates="item_type", cascade="all, delete-orphan")


class GameAccounts(TimestampMixin, Base):
    __tablename__ = "game_accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    #TODO: добавить связь с юзером подумать над полями

    account_items: Mapped[list["Item"]] = relationship(back_populates="account", cascade="all, delete-orphan")


class Market(TimestampMixin, Base):
    __tablename__ = "markets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    #TODO: добавить поле логотипа

    market_items: Mapped[list["Item"]] = relationship(back_populates="market", cascade="all, delete-orphan")


class ItemFloat(TimestampMixin, Base):
    __tablename__ = "item_floats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, index=True)
    abbr: Mapped[str] = mapped_column(String(2), unique=True, nullable=False, index=True)
    min_value: Mapped[float] = mapped_column(Float, nullable=False)
    max_value: Mapped[float] = mapped_column(Float, nullable=False)

    float_items: Mapped[list["Item"]] = relationship(back_populates="item_float", cascade="all, delete-orphan")
