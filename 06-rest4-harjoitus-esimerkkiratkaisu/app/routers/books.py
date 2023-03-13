from fastapi import APIRouter, status, Depends
from ..database.schemas import BookDb, BookIn
from ..database.crud import fetch_book, save_book, remove_book, fetch_books, fetch_books_by_author
from sqlalchemy.orm import Session
from ..database.database import SessionLocal

router = APIRouter(prefix='/books', tags=['books'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('', response_model=list[BookDb])
def get_books(author_name: str = '', db: Session = Depends(get_db)):
    if author_name != '':
        return fetch_books_by_author(db, author_name)
    else:
        bs = fetch_books(db)
        return bs


@router.post('', status_code=status.HTTP_201_CREATED, response_model=BookDb)
def create_book(book_in: BookIn, db: Session = Depends(get_db)):
    return save_book(db, book_in)


@router.get('/{id}', response_model=BookDb)
def get_book(id: int, db: Session = Depends(get_db)):
    book = fetch_book(db, id)
    return book


@router.delete('/books/{id}')
def delete_book(id: int, db: Session = Depends(get_db)):
    remove_book(db, id)
    return {'message': 'deleted'}
