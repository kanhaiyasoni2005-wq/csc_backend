from pydantic import BaseModel,ConfigDict
from app.schemas.service import ServiceResponse
class applicationSchema(BaseModel):
     
        service_id:int
       
        price:float
        
        # order_id:int
        images:list[str]
class applicationResponse(applicationSchema):
        id:int
        service:ServiceResponse
        order_id:int
        model_config  = ConfigDict(from_attributes=True)


class orderSchema(BaseModel):
     
        user_id:int
class orderResponse(orderSchema):
      id:int
     
      application:list[applicationResponse] = []

