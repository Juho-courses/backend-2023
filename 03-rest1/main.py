from fastapi import FastAPI

app = FastAPI()

numbers = [1, 2, 3, 4, 5]

# /numbers/0


@app.get('/numbers/{id}')
def get_number(id: int):
    return numbers[id]


# /numbers
# /numbers?count=2
@app.get('/numbers')
def get_numbers(count: int = -1):
    print(count)
    return numbers


@app.get('/')
def root():
    return {'message': 'hello'}
