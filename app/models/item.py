from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Float
from sqlalchemy import Enum as SAEnum

from app.models.mixins import TimestampMixin
from app.db.base import Base


class ItemStatus(str, Enum):
    ITEM_SOLD = "sold"
    ITEM_STORAGE = "storage"
    ITEM_LISTED = "listed"


class Item(TimestampMixin, Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("item_types.id", ondelete="CASCADE"), nullable=False)
    float_id: Mapped[int] = mapped_column(Integer, ForeignKey("item_floats.id", ondelete="CASCADE"), nullable=True)
    float_value: Mapped[float] = mapped_column(Float, nullable=False)
    purchase_price: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    sale_price: Mapped[float] = mapped_column(Float, nullable=True, index=True)
    status: Mapped[ItemStatus] = mapped_column(SAEnum(ItemStatus), default=ItemStatus.ITEM_STORAGE, index=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("game_accounts.id", ondelete="CASCADE"), nullable=False)
    market_id: Mapped[int] = mapped_column(Integer, ForeignKey("markets.id", ondelete="CASCADE"), nullable=True)

    item_type: Mapped["ItemType"] = relationship(back_populates="type_items")
    item_float: Mapped["ItemFloat"] = relationship(back_populates="float_items")
    account: Mapped["GameAccounts"] = relationship(back_populates="account_items")
    market: Mapped["Market"] = relationship(back_populates="market_items")

