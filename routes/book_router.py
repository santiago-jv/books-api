from fastapi import APIRouter,HTTPException
from models.book import BookDTO
from database.data import books


from database.connection import client
from schemas.book import Books


book_router = APIRouter(prefix='/books')

    
@book_router.get('/')
def get_books():
    books = client.execute(Books.select()).fetchall()
    return books

@book_router.post('/',status_code=201)
def create_book(new_book:BookDTO):
    result =  client.execute(Books.insert().values(new_book.dict()))
    book_id = result.inserted_primary_key[0]
    book = client.execute(Books.select().where(Books.c.id == book_id)).first()
    
    return book
    
@book_router.get('/{id}')
def get_book(id:str):
    book = client.execute(Books.select().where(Books.c.id == id)).first()
    if(not book):
        raise HTTPException(status_code=404, detail="Book not found")
        
    return book
    
@book_router.put('/{id}')
def update_book(id:str, new_book:BookDTO):
    book = client.execute(Books.select().where(Books.c.id == id)).first()
    if(not book):
        raise HTTPException(status_code=404, detail="Book not found")
    
    
    client.execute(Books.update().values(new_book.dict()).where(Books.c.id == id))
    
    return "Book updated successfully"
    
    

@book_router.delete('/{id}')
def delete_book(id:str):

    book = client.execute(Books.select().where(Books.c.id == id)).first()
    if(not book):
        raise HTTPException(status_code=404, detail="Book not found")
    
    client.execute(Books.delete().where(Books.c.id == id))
    
        
    return {"message":"Book deleted successfully"}

