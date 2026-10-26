from fastapi import APIRouter, Depends, HTTPException,status
from app.core.db import get_db
from app.schemas.category import CategorySchema,CategoryResponse
from sqlalchemy.orm import Session

from app.services.category import category_fatch, create_cate


category_routes = APIRouter(prefix="/category",tags=["Category"])

@category_routes.post("/create",status_code=status.HTTP_201_CREATED,response_model=CategoryResponse)
def create_category(data:CategorySchema, db:Session = Depends(get_db)):
    return create_cate(data,db)

@category_routes.get("/fatch",status_code=status.HTTP_200_OK, response_model=list[CategoryResponse])
def fatch_category(db:Session = Depends(get_db)):
    return category_fatch(db)
