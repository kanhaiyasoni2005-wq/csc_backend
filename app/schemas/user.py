from pydantic import BaseModel, ConfigDict

class userSchema(BaseModel):
     name:str
     phone:str
     email:str
     password:str

class userResponse(BaseModel):
     id:int
     name:str
     phone:str
     email:str
     password:str
     model_config = ConfigDict(from_attributes=True)

class loginSchema(BaseModel):
     email:str
     password:str