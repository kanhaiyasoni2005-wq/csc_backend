from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Float
from typing import TYPE_CHECKING
from app.core.db import Base
if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.application import Application

class Service(Base):
    __tablename__ = "service"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String)
    description:Mapped[str] = mapped_column(String)
    price:Mapped[float] = mapped_column(Float)
    category_id:Mapped[int] = mapped_column(ForeignKey("category.id"))
    category:Mapped["Category"]= relationship(back_populates="service")
    application:Mapped["Application"] = relationship(back_populates="service",cascade="all,delete-orphan")