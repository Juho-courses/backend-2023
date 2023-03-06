from fastapi import APIRouter, status
from ..database.models import BookDb, BookIn
from ..database.database import books, fetch_book, save_book, remove_book

router = APIRouter(prefix='/books', tags=['books'])


@router.get('', response_model=list[BookDb])
def get_books(author_name: str = ''):
    if author_name != '':
        return [b for b in books if b['author'] == author_name]
    else:
        return books


@router.post('', status_code=status.HTTP_201_CREATED, response_model=BookDb)
def create_book(book_in: BookIn):
    return save_book(book_in)


@router.get('/{id}', response_model=BookDb)
def get_book(id: int):
    return fetch_book(id)


@router.delete('/{id}')
def delete_book(id: int):
    remove_book(id)
    return {'message': 'deleted'}
