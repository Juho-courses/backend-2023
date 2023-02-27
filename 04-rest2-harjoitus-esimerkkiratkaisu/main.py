from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class BookIn(BaseModel):
    title: str
    author: str


class BookDb(BookIn):
    id: int


books = [
    {'id': 0, 'title': 'k1', 'author': 'a1'},
    {'id': 1, 'title': 'k2', 'author': 'a2'},
    {'id': 2, 'title': 'k3', 'author': 'a1'},
]


@app.get('/books', response_model=list[BookDb])
def get_books(author_name: str = ''):
    if author_name != '':
        return [b for b in books if b['author'] == author_name]
    else:
        return books


@app.post('/books', status_code=status.HTTP_201_CREATED, response_model=BookDb)
def create_book(book_in: BookIn):
    new_id = len(books)
    book = BookDb(**book_in.dict(), id=new_id)
    books.append(book.dict())
    return book


@app.get('/books/{id}', response_model=BookDb)
def get_book(id: int):
    index = -1
    for i, v in enumerate(books):
        if v['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="not found", status_code=404)
    return books[index]


@app.delete('/books/{id}')
def delete_book(id: int):
    index = -1
    for i, v in enumerate(books):
        if v['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="not found", status_code=404)
    del books[index]
    return {'message': 'deleted'}
