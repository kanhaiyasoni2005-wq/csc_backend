import httpx

from app.core.config import settings


async def create_cashfree_order(payment):
    payload = {
        "order_id": payment.order_id,
        "order_amount": float(payment.amount),
        "order_currency": payment.currency,
        "customer_details": {
            "customer_id": payment.customer_id,
            "customer_email": payment.customer_email,
            "customer_phone": payment.customer_phone,
        },
    }

    headers = {
        "x-client-id": settings.CASHFREE_APP_ID,
        "x-client-secret": settings.CASHFREE_SECRET_KEY,
        "x-api-version": "2025-01-01",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            f"{settings.CASHFREE_BASE_URL}/orders",
            json=payload,
            headers=headers,
        )

    if response.status_code not in (200, 201):
        raise ValueError("Cashfree order creation failed")

    return response.json()

async def fetch_cashfree_payments(order_id: str):
    headers = {
        "x-client-id": settings.CASHFREE_APP_ID,
        "x-client-secret": settings.CASHFREE_SECRET_KEY,
        "x-api-version": "2025-01-01",
        "Content-Type": "application/json",
    }

    url = (
        f"{settings.CASHFREE_BASE_URL.rstrip('/')}"
        f"/orders/{order_id}/payments"
    )

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            url,
            headers=headers,
        )

    print("Cashfree status code:", response.status_code)
    print("Cashfree response:", response.text)

    if response.status_code != 200:
        raise ValueError(
            f"Cashfree error {response.status_code}: {response.text}"
        )

    return response.json()