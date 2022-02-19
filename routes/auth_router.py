from database.connection import get_database
from fastapi import APIRouter, HTTPException,Depends
import bcrypt
from sqlalchemy.orm import Session
import jwt
from models.user import RegisterUserDTO, LoginUserDTO
from schemas.user import User
from repositories.user_repository import create_user, get_user_by_email
from constants import JWT_SECRET_KEY


auth_router = APIRouter(prefix='/auth')

@auth_router.post('/register', status_code=201)
def register_user(user:RegisterUserDTO, database:Session = Depends(get_database)):
    result = get_user_by_email(database,user.email)
    if(result):
        raise HTTPException(status_code=400, detail="The Email already exist")
    
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes(user.password,"utf-8"), salt)
    user.password = hashed_password
    
    new_user = create_user(database,user)
    del new_user.password
    token = jwt.encode({'id': new_user.id}, JWT_SECRET_KEY)
    return { "user":new_user.__dict__,"token": token}  
    
@auth_router.post('/login')
def login_user(user:LoginUserDTO,database:Session = Depends(get_database)):
    user_data:User = get_user_by_email(database,user.email)
    if(not user_data):
        raise HTTPException(status_code=400, detail="The Email no exist")
    
  
    if(bcrypt.checkpw(user.password.encode("utf-8"), user_data.password)):
        token = jwt.encode({'id': user_data.id}, JWT_SECRET_KEY)
        del user_data.password
        return { "user":user_data.__dict__,"token": token}  
    
    raise HTTPException(status_code=401, detail="Unauthorized")
    