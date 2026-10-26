from pydantic import BaseModel, ConfigDict

class ServiceSchema(BaseModel):   
        name:str
        description:str
        price:float
        category_id:int
class ServiceResponse(ServiceSchema):
        id:int
        model_config = ConfigDict(from_attributes=True)