from typing import Text,Optional
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel


  
class BookDTO(BaseModel):
    title:str 
    description:Text
    author:str 
    
