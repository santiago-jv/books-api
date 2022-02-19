from sqlalchemy.orm import Session
from models.user import RegisterUserDTO
from schemas.user import User

def get_user_by_email(database:Session, email:str):
    user = database.query(User).filter(User.email == email).first()
    return user
def get_user_by_id(database:Session, id:int):
    user = database.query(User).filter(User.id == id).first()
    return user

def create_user(database:Session, user:RegisterUserDTO):
    new_user = User(email=user.email, name=user.name, password=user.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    
    return new_user