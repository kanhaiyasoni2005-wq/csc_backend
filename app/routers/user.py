from fastapi import APIRouter, Request, status, Depends
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.schemas.user import userResponse,userSchema,loginSchema
from app.services.user import user_create, user_login
from app.services.user import is_authentication
user_routes = APIRouter(prefix="/user", tags=["User"])

@user_routes.post("/create",status_code=status.HTTP_201_CREATED, response_model=userResponse)
def create_user(data:userSchema, db:Session = Depends(get_db)):
    return user_create(data,db)
@user_routes.post("/login")
def login(data:loginSchema, db:Session = Depends(get_db)):
    return user_login(data,db)
@user_routes.get("/is_auth",status_code=status.HTTP_200_OK,response_model=userResponse)
def Authentication(request:Request,db:Session = Depends(get_db)):
    return is_authentication(request , db)