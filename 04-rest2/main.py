from fastapi import FastAPI, status, HTTPException

from pydantic import BaseModel

app = FastAPI()


class NumberIn(BaseModel):
    number: int


class NumberDb(NumberIn):
    id: int


numbers = [
    {'id': 0, 'number': 123},
    {'id': 1, 'number': 1231},
    {'id': 2, 'number': 123192},
]

# /numbers/0


@app.get('/numbers/{id}')
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


# /numbers
# /numbers?count=2
@app.get('/numbers', response_model=list[NumberDb])
def get_numbers(count: int = -1):
    print(count)
    return numbers


@app.post('/numbers', response_model=NumberDb, status_code=status.HTTP_201_CREATED)
def create_number(number_in: NumberIn):
    new_id = len(numbers)
    number = NumberDb(**number_in.dict(), id=new_id)
    numbers.append(number.dict())
    return number


@app.get('/')
def root():
    return {'message': 'hello'}
