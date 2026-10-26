from sqlalchemy.orm import Session 
from app.schemas.order import applicationSchema
from app.models.order import orders
from app.models.application import Application
from app.schemas.user import userResponse
import json
def order_add(data: applicationSchema, db: Session, user: userResponse):
    print("INPUT IMAGES:", type(data.images), data.images)

    order = db.query(orders).filter(
        orders.user_id == user.id
    ).first()

    if order is None:
        order = orders(user_id=user.id)
        db.add(order)
        db.flush()

    new_application = Application(
        service_id=data.service_id,
        price=data.price,
        order_id=order.id,
        images=data.images
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    print("DATABASE IMAGES:", type(new_application.images))
    print("DATABASE VALUE:", new_application.images)

    return new_application
def get_application(db:Session,user_id:int):
   fatchd = db.query(orders).filter(orders.user_id == user_id).all()
   return fatchd
