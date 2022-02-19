from dotenv import load_dotenv
import os

load_dotenv()


DATABASE_URL='postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'.format(
                    DATABASE_USER=os.environ.get("DATABASE_USER"),
                    DATABASE_PASSWORD=os.environ.get("DATABASE_PASSWORD"),
                    DATABASE_NAME=os.environ.get("DATABASE_NAME"),
                    DATABASE_HOST=os.environ.get("DATABASE_HOST"))
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
