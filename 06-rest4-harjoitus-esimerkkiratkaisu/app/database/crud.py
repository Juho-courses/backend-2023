from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models


def save_author(db: Session, author_in):
    author = models.Author(**author_in.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def fetch_author(db: Session, id):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if author is None:
        raise HTTPException(
            status_code=404, detail=f"Author with id {id} not found")
    return author


def fetch_authors(db: Session):
    return db.query(models.Author).all()


def fetch_book(db: Session, id):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if book is None:
        raise HTTPException(
            status_code=404, detail=f"book with id {id} not found")
    return book


def fetch_books_by_author(db: Session, author: str):
    books = db.query(models.Book).filter(models.Book.author == author).all()
    return books


def fetch_books(db: Session):
    return db.query(models.Book).all()


def save_book(db: Session, book_in):
    book = models.Book(**book_in.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def remove_book(db: Session, id):
    book = fetch_book(db, id)
    db.delete(book)
    db.commit()
