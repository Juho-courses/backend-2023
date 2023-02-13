from fastapi import FastAPI

app = FastAPI()

books = [
    {'id': 0, 'title': 'k1', 'author': 'a1'},
    {'id': 1, 'title': 'k2', 'author': 'a2'},
    {'id': 2, 'title': 'k3', 'author': 'a1'},
]


@app.get('/books')
def get_books(author_name: str = ''):
    if author_name != '':
        return [b for b in books if b['author'] == author_name]
    else:
        return books


@app.get('/books/{id}')
def get_book(id: int):
    return books[id]
