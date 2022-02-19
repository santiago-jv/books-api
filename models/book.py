from typing import Text
from pydantic import BaseModel


  
class BookDTO(BaseModel):
    title:str 
    description:Text
    author:str 
    user_id:int
class UpdateBookDTO(BaseModel):
    title:str 
    description:Text
    author:str 