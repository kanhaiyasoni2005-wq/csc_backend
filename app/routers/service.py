from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.service import ServiceResponse, ServiceSchema
from app.core.db import get_db
from app.services.service import fatch_service, fatch_using_category, service_create

service_routes = APIRouter(prefix="/service",tags=["Services"])

@service_routes.post("/create",status_code=status.HTTP_201_CREATED, response_model=ServiceResponse)
def create_service(data:ServiceSchema, db:Session = Depends(get_db)):
    return service_create(data, db)
@service_routes.get("/fatch",status_code=status.HTTP_200_OK,response_model= list[ServiceResponse] )
def find_service(db:Session = Depends(get_db)):
    return fatch_service(db)
@service_routes.get("/fatch_by_category{id}",status_code=status.HTTP_200_OK,response_model=list[ServiceResponse] )
def fatch_by_category(id:int, db:Session = Depends(get_db)):
    return fatch_using_category(id,db)