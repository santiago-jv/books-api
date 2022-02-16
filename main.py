
from fastapi import FastAPI
from routes.book_router import book_router
    
app = FastAPI()
app.include_router(book_router)

@app.get('/')
def home():
    return {"Message": "Welcome to my BOOKS API EXAMPLE. Go to /docs for look documentation"}
