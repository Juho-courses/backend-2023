from fastapi import HTTPException, status, APIRouter
from ..database.models import NumberDb, NumberIn
from ..database.database import numbers, save_number

router = APIRouter(prefix='/numbers', tags=['numbers'])


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
def get_numbers(count: int = -1):
    return numbers


@router.post('', response_model=NumberDb, status_code=status.HTTP_201_CREATED)
def create_number(number_in: NumberIn):
    return save_number(number_in)
