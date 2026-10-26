from fastapi import APIRouter, Depends, status
from app.schemas.order import applicationSchema
from app.core.db import get_db
from sqlalchemy.orm import Session
from helper import is_authenticated
from app.services.order import get_application, order_add
from app.schemas.user import userResponse
from app.schemas.order import orderResponse
from app.schemas.order import applicationResponse
application_route = APIRouter(prefix=("/application"), tags=["Application"])

@application_route.post("/create",status_code= status.HTTP_201_CREATED, response_model=applicationResponse )
def create_order(data:applicationSchema,db:Session = Depends(get_db),user:userResponse = Depends(is_authenticated)):
    return order_add(data,db,user)
@application_route.get("/fatch",status_code= status.HTTP_200_OK, response_model= list[orderResponse])
def fatch_order(db:Session = Depends(get_db),user:userResponse = Depends(is_authenticated)):
    return get_application(db,user.id)