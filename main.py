
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from database.connection import Base,engine
from routes.auth_router import auth_router
from routes.book_router import book_router
from constants import JWT_SECRET_KEY
from starlette.responses import JSONResponse
import jwt
from starlette.datastructures import MutableHeaders

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)        
app.include_router(auth_router)

@app.middleware("http")
async def verify_authorization(request:Request, call_next):
    if "auth" in request.url.path or "/" ==  request.url.path:
        response = await call_next(request)     
        return response  
    try:
        token = request.headers["Authorization"]
        print(token)
        user = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
     
       
        response = await call_next(request)     
        return response   
    except KeyError:
        return JSONResponse(content={"message":"Token not provided"}, status_code=401)
    except jwt.ExpiredSignatureError:
        return JSONResponse(content={"message":"Token expired"}, status_code=401)
    except jwt.DecodeError:
        return JSONResponse(content={"message":"Invalid token"}, status_code=401)
    
    
app.include_router(book_router)



@app.get('/')
def home():
    return {"Message": "Welcome to my BOOKS API EXAMPLE. Go to /docs for look documentation"}
