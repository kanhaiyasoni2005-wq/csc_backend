from app.schemas.category import CategorySchema
from sqlalchemy.orm import Session
from app.models.category import Category

def create_cate(data:CategorySchema,db:Session):
    new_category = Category(
        image_url = data.image_url,
        name = data.name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def category_fatch(db:Session):
    data = db.query(Category).all()
    return data