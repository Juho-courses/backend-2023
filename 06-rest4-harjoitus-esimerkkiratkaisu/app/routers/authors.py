from fastapi import APIRouter, status, Depends
from ..database.schemas import AuthorBase, AuthorDb
from ..database.crud import save_author, fetch_author, fetch_authors
from ..database.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix='/authors', tags=['authors'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('', response_model=list[AuthorDb])
def get_authors(db: Session = Depends(get_db)):
    return fetch_authors(db)


@router.post('', response_model=AuthorDb, status_code=status.HTTP_201_CREATED)
def create_author(author_in: AuthorBase, db: Session = Depends(get_db)):
    return save_author(db, author_in)


@router.get('/{id}', response_model=AuthorDb)
def get_author(id: int, db: Session = Depends(get_db)):
    return fetch_author(db, id)
