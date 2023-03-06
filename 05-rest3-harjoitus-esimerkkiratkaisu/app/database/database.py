from fastapi import HTTPException
from .models import AuthorDb, BookDb

authors = [
    {'id': 0, 'name': 'a1'},
    {'id': 1, 'name': 'a2'},
]

books = [
    {'id': 0, 'title': 'k1', 'author': 'a1'},
    {'id': 1, 'title': 'k2', 'author': 'a2'},
    {'id': 2, 'title': 'k3', 'author': 'a1'},
]


def save_author(author_in):
    new_id = len(authors)
    author = AuthorDb(**author_in.dict(), id=new_id)
    authors.append(author.dict())
    return author


def fetch_author(id):
    return authors[get_authors_index(id)]


def get_authors_index(id):
    index = -1
    for i, v in enumerate(authors):
        if v['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="not found", status_code=404)
    return index


def get_book_index(id):
    index = -1
    for i, v in enumerate(books):
        if v['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="not found", status_code=404)
    return index


def fetch_book(id):
    return books[get_book_index(id)]


def save_book(book_in):
    new_id = len(books)
    book = BookDb(**book_in.dict(), id=new_id)
    books.append(book.dict())
    return book


def remove_book(id):
    del books[get_book_index(id)]
