from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
load_dotenv()
import os

metadata = MetaData()


   
load_dotenv()


engine = create_engine('postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
                       .format( 
                                DATABASE_USER=  os.environ.get("DATABASE_USER"),
                                DATABASE_PASSWORD=  os.environ.get("DATABASE_PASSWORD"),
                                DATABASE_NAME= os.environ.get("DATABASE_NAME"),
                                 DATABASE_HOST = os.environ.get("DATABASE_HOST"),
))
client = engine.connect()