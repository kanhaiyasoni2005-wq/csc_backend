from fastapi import status
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.application import Application
    from app.models.user import user
from app.core.db import Base
class orders(Base):
    __tablename__ = "orders"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    user:Mapped["user"] = relationship(back_populates="orders")    
    application:Mapped[list["Application"]] = relationship(back_populates="order", cascade="all,delete-orphan")