from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
load_dotenv()
import os

metadata = MetaData()

print('postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}'
                       .format( 
                                DATABASE_USER=  os.environ.get("DATABASE_USER"),
                                DATABASE_PASSWORD=  os.environ.get("DATABASE_PASSWORD"),
                                DATABASE_NAME= os.environ.get("DATABASE_NAME"),
))

   
load_dotenv()


engine = create_engine('postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}'
                       .format( 
                                DATABASE_USER=  os.environ.get("DATABASE_USER"),
                                DATABASE_PASSWORD=  os.environ.get("DATABASE_PASSWORD"),
                                DATABASE_NAME= os.environ.get("DATABASE_NAME"),
))
client = engine.connect()