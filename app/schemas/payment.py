from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class PaymentRequest(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    customer_id: str
    customer_email: EmailStr
    customer_phone: str


class PaymentResponse(BaseModel):
    id: int
    order_id: str
    amount: Decimal
    status: str
    payment_session_id: str | None = None
    model_config = ConfigDict(from_attributes=True)