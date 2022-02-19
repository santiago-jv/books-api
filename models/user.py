
from pydantic import BaseModel


  
class RegisterUserDTO(BaseModel):
    name:str
    email:str
    password:str
    
    
class LoginUserDTO(BaseModel):
    email:str
    password:str