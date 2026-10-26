from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String,Integer,Float
from app.core.db import settings, Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.order import orders


class user(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key= True)
    name:Mapped[str] = mapped_column(String)
    phone:Mapped[str] = mapped_column(String)
    email:Mapped[str] = mapped_column(String)
    password:Mapped[str] = mapped_column(String)
    orders:Mapped["orders"] = relationship(back_populates="user",cascade="all,delete-orphan")