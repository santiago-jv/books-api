import datetime
from sqlalchemy.sql.sqltypes import String,Integer, DateTime, Text
from sqlalchemy import  Column,ForeignKey
from database.connection import Base
from sqlalchemy.orm import relationship


class Book(Base):
  __tablename__ = 'books'
  
  id=Column( Integer, primary_key=True, autoincrement=True)
  title=Column( String, nullable=False)
  description=Column( Text, nullable=False)
  author=Column( String, nullable=False)
  created_at = Column( DateTime, default=datetime.datetime.now())
  
  user_id = Column( Integer, ForeignKey("users.id"))
  user = relationship("User", back_populates="books") 
