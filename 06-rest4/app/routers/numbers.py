from sqlalchemy.orm import Session
from fastapi import HTTPException, status, APIRouter, Depends
from ..database.schemas import NumberDb, NumberIn
from ..database import crud_numbers
from ..database.database import SessionLocal

router = APIRouter(prefix='/numbers', tags=['numbers'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/{id}')
def get_number(id: int):
    index = -1
    for i, number in enumerate(numbers):
        if number['id'] == id:
            index = i
            break
    if index == -1:
        # ei löytynyt
        raise HTTPException(detail="not found", status_code=404)
    return numbers[index]


@router.get('', response_model=list[NumberDb])
def get_numbers(db: Session = Depends(get_db)):
    return crud_numbers.read_numbers(db)


@router.post('', response_model=NumberDb, status_code=status.HTTP_201_CREATED)
def create_number(number_in: NumberIn, db: Session = Depends(get_db)):
    return crud_numbers.create_number(db, number_in)
