from sqlalchemy.orm import Session
from schemas.book import  Book
from models.book import BookDTO,UpdateBookDTO
from .user_repository import get_user_by_id
def retrieve_book(database:Session, id:int):
    return database.query(Book).filter(Book.id == id).first()

def retrieve_books(database:Session):
    return database.query(Book).all()
def retrieve_books_by_user_id(database:Session, user_id:int):
    return database.query(Book).filter(Book.user_id == user_id).all()
    
def save_book(database:Session,book:BookDTO):
    user = get_user_by_id(database,book.user_id)
    if(not user):
        return None
    book = Book(title=book.title, description=book.description, author=book.author,user_id=book.user_id)
    database.add(book)
    database.commit()
    database.refresh(book)
    return book

def update_book_object(database:Session,id:int, new_book:UpdateBookDTO):
    book = database.query(Book).filter(Book.id==id).update(new_book.dict())
    print(book)
    database.commit()
    return book

def remove_book(database:Session,id:int):
    book=database.query(Book).filter(Book.id==id).first()
    
    if(not book):
        return False
    
    database.delete(book)
    database.commit()
    return True
    

        