from fastapi import APIRouter, status
from ..database.models import AuthorBase, AuthorDb
from ..database.database import authors, save_author, fetch_author

router = APIRouter(prefix='/authors', tags=['authors'])


@router.get('', response_model=list[AuthorDb])
def get_authors():
    return authors


@router.post('', response_model=AuthorDb, status_code=status.HTTP_201_CREATED)
def create_author(author_in: AuthorBase):
    return save_author(author_in)


@router.get('/{id}', response_model=AuthorDb)
def get_author(id: int):
    return fetch_author(id)
