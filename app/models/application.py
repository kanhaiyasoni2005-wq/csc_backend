
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, ForeignKey, JSON
from app.core.db import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.order import orders
    from app.models.services import Service

class Application(Base):
    __tablename__ = "application"

    id:Mapped[int] = mapped_column(primary_key=True)
    service_id:Mapped[int] = mapped_column(ForeignKey("service.id"))
    service:Mapped["Service" ]= relationship(back_populates="application")
    price:Mapped[float] = mapped_column(Float)
    order:Mapped["orders"] = relationship(back_populates="application")
    order_id:Mapped[int] = mapped_column(ForeignKey("orders.id"))   
    images:Mapped[list[str]] = mapped_column(JSON)