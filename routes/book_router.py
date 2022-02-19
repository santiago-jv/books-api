from fastapi import APIRouter,HTTPException, Depends
from models.book import BookDTO,UpdateBookDTO
from database.connection import get_database
from repositories.book_repository import retrieve_books,save_book,retrieve_book,remove_book,update_book_object,retrieve_books_by_user_id
from sqlalchemy.orm import Session
book_router = APIRouter(prefix='/books')
 

@book_router.get('/')
def get_books(database:Session = Depends(get_database)):
    books = retrieve_books(database)
    return books
@book_router.get('/user/{user_id}')
def get_books_by_user_id(user_id:int,database:Session = Depends(get_database)):
    books = retrieve_books_by_user_id(database,user_id)
    return books
    
@book_router.post('/',status_code=201)
def create_book(new_book:BookDTO,database:Session = Depends(get_database)):
    book = save_book(database, new_book)
    
    if(not book):
        raise HTTPException(status_code=500, detail="Book not created")
    
    return book

@book_router.get('/{id}')
def get_book(id:int, database:Session = Depends(get_database)):
    book = retrieve_book(database, id)
    if(not book):
        raise HTTPException(status_code=404, detail="Book not found")
        
    return book

@book_router.put('/{id}')
def update_book(id:int, new_book:UpdateBookDTO, database:Session = Depends(get_database)):
    book_id =update_book_object(database, id, new_book)
    if(not book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    
    return "Book updated successfully"
    
    



@book_router.delete('/{id}')
def delete_book(id:int, database:Session = Depends(get_database)):
    result = remove_book(database, id)
    if(not result):
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {"message":"Book deleted successfully"}