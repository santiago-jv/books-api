from fastapi import APIRouter,HTTPException
from models.book import Book, BookUpdateDTO, CreateBookDTO
from database.data import books
book_router = APIRouter(prefix='/books')

    
@book_router.get('/')
def get_books():
    return {"books":books}

@book_router.post('/',status_code=201)
def create_book(new_book:CreateBookDTO):
    book = Book(title=new_book.title, description=new_book.description)
    
    books.append(book.dict())
    print(book.dict())
    
    return book.dict()

@book_router.get('/{id}')
def get_book(id:str):
    for book in books:
        if book["id"] == id:
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")
    

@book_router.put('/{id}')
def update_book(id:str, new_book:BookUpdateDTO):
    
    for book in books:
        if book["id"] == id:
            book["description"] = new_book.description
            book["title"] =new_book.title
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.delete('/{id}')
def delete_book(id:str):
    for index,book in books:
        if book["id"] == id:
            books.pop(index)
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")
        
