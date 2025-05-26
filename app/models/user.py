# import uuid
#
# from enum import Enum
#
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import String
#
# from app.models.mixins import TimestampMixin
# from app.db.base import Base
#
#
# class PortalRole(str, Enum):
#     ROLE_USER = "user"
#     ROLE_ADMIN = "admin"
#     ROLE_ROOT = "root"
#
#
# class User(TimestampMixin, Base):
#     __tablename__ = "users"
#
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
#     role: Mapped[str] = mapped_column(String(30), nullable=False)
#
#     @property
#     def is_user(self):
#         return PortalRole.ROLE_USER == self.role
#
#     @property
#     def is_admin(self):
#         return PortalRole.ROLE_ADMIN == self.role
#
#     @property
#     def is_root(self):
#         return PortalRole.ROLE_ROOT == self.role
