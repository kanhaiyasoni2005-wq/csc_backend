from sqlalchemy.orm import Mapped , mapped_column, relationship
from sqlalchemy import (
    String,
    Integer,
    Float
)
from app.core.db import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.services import Service

class Category(Base):
    __tablename__ = "category"
    id:Mapped[int] = mapped_column(primary_key=True)
    image_url:Mapped[str] = mapped_column(String)
    name:Mapped[str]= mapped_column(String)
    service:Mapped[list["Service"]] = relationship(back_populates="category",cascade="all,delete-orphan")
