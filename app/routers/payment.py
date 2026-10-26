from fastapi import APIRouter, Depends, HTTPException
import httpx
from sqlalchemy.orm import Session
from app.services.payment import (
    create_cashfree_order,
    fetch_cashfree_payments,
)

from app.core.db import get_db
from app.models.payment import PaymentOrder
from app.schemas.payment import PaymentRequest, PaymentResponse
from app.services.payment import create_cashfree_order
from cashfree_pg.api_client import Cashfree

payment_router = APIRouter(prefix="/payment", tags=["Payment"])


@payment_router.post("/create", response_model=PaymentResponse)
async def create_payment(
    data: PaymentRequest,
    db: Session = Depends(get_db),
):
    payment = PaymentOrder(
        customer_id=data.customer_id,
        customer_email=str(data.customer_email),
        customer_phone=data.customer_phone,
        amount=data.amount,
        status="PENDING",
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    try:
        result = await create_cashfree_order(payment)

        payment.payment_session_id = result["payment_session_id"]
        payment.order_id = result["order_id"]
        db.commit()
        db.refresh(payment)
        payment.order_id

    except (ValueError, KeyError):
        payment.status = "CREATE_FAILED"
        db.commit()

        raise HTTPException(
            status_code=502,
            detail="Cashfree order create nahi hua",
        )

    return payment


@payment_router.post("/verify/{payment_id}")
async def verify_payment(
    payment_id: int,
    db: Session = Depends(get_db),
):
    payment = db.get(PaymentOrder, payment_id)

    if not payment:
        raise HTTPException(404, "Payment not found")

    if not payment.order_id:
        raise HTTPException(400, "Cashfree order ID missing")

    try:
        payments = await fetch_cashfree_payments(payment.order_id)
    except (ValueError, httpx.HTTPError) as e:
        raise HTTPException(
            status_code=502,
            detail="Cashfree se payment status fetch nahi hua",
        ) from e

    for item in payments:
        if item.get("payment_status") == "SUCCESS":
            payment.status = "SUCCESS"
            db.commit()
            db.refresh(payment)

            return {
                "payment_id": payment.id,
                "order_id": payment.order_id,
                "status": payment.status,
                "message": "Payment verified successfully",
            }

    return {
        "payment_id": payment.id,
        "order_id": payment.order_id,
        "status": payment.status,
        "message": "Payment abhi successful nahi hai",
    }