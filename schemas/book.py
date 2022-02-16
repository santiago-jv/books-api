import datetime
from sqlalchemy.sql.sqltypes import String,Integer, DateTime, Text
from database.connection import metadata, engine
from sqlalchemy import Table, Column

Books = Table('books', metadata, 
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('title', String, nullable=False),
              Column('description', Text, nullable=False),
              Column('author', String, nullable=False),
              Column('create_at', DateTime, default=datetime.datetime.now())
            )

metadata.create_all(engine)