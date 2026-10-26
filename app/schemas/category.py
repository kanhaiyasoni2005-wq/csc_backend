from pydantic import BaseModel ,ConfigDict
from app.schemas.service import ServiceResponse

class CategorySchema(BaseModel):
        image_url:str
        name:str
        

class CategoryResponse(CategorySchema):
        id:int
        # services:list[ServiceResponse]
        model_config = ConfigDict(from_attributes=True)

# class CategoryResponsefor(CategorySchema):
#         id:int
#         services:list[ServiceResponse]
#         model_config = ConfigDict(from_attributes=True)