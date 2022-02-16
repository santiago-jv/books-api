
from fastapi import FastAPI,HTTPException
from models.book import Book, BookUpdateDTO, CreateBookDTO

books = []
    
app = FastAPI()


@app.get('/')
def home():
    return "Hi"
    
@app.get('/books')
def get_books():
    return {"books":books}

@app.post('/books',status_code=201)
def create_book(new_book:CreateBookDTO):
    book = Book(title=new_book.title, description=new_book.description)
    
    books.append(book.dict())
    print(book.dict())
    
    return book.dict()

@app.get('/books/{id}')
def get_book(id:str):
    for book in books:
        if book["id"] == id:
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")
    

@app.put('/books/{id}')
def update_book(id:str, new_book:BookUpdateDTO):
    
    for book in books:
        if book["id"] == id:
            book["description"] = new_book.description
            book["title"] =new_book.title
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete('/books/{id}')
def delete_book(id:str):
    for index,book in books:
        if book["id"] == id:
            books.pop(index)
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")
        