import datetime
from sqlalchemy.sql.sqltypes import String,Integer, DateTime,LargeBinary
from database.connection import Base
from sqlalchemy import  Column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
  
    id=Column( Integer, primary_key=True, autoincrement=True)
    name=Column( String, nullable=False)
    email=Column( String, nullable=False,unique=True)
    password=Column( LargeBinary , nullable=False)
    created_at = Column( DateTime, default=datetime.datetime.now())
    
    books = relationship("Book", back_populates="user")


