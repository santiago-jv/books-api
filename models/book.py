from typing import Text,Optional
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel

class Book(BaseModel):
    id:str = uuid4().__str__()
    title:str
    description:Text
    created_at:datetime = datetime.now()
  
  
  
class CreateBookDTO(BaseModel):
    title:str 
    description:Text
    
    
class BookUpdateDTO(BaseModel):
    id:str
    title:str
    description:Text
    created_at:datetime