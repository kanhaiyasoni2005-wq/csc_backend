from app.schemas.service import ServiceSchema
from sqlalchemy.orm import Session
from app.models.services import Service

def  service_create(data:ServiceSchema, db:Session):
    new_service =  Service(
         name = data.name,
        description = data.description,
        price = data.price,
        category_id = data.category_id

    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service
def fatch_service(db:Session):
    data = db.query(Service).all()
    return data
def fatch_using_category(id:int,db:Session):
    data = db.query(Service).filter(Service.category_id == id).all()
    return data