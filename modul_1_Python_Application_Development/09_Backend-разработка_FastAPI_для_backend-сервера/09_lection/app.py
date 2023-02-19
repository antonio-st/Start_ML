import datetime
from fastapi import FastAPI, HTTPException # импорт fastapi и модуля ошибок HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor  # класс для превращения ответа БД в словарь(dict)
from pydantic import BaseModel # pydantic библиотека для валидации типов
from loguru import logger
from typing import List

app = FastAPI()  # экземпляр класса FastAPI


# валидация для @app.post('/user/validate')
class SimpleUser(BaseModel):
    first_name: str
    last_name: str
    age: int

# валидация для @app.get('/booking/all)
class BookingGet(BaseModel):
    id: int
    facility_id: int
    member_id: int
    start_time: datetime.datetime
    slots: int

    class Config:
        orm_mode = True

@app.get('/', summary='Just say welcome to user')
def say_hello():
    """
    Doc for end point in Swagger
    """
    return 'Welcome to FastAPI'


@app.get('/sum')  # sum?a=10&b=20
def num_sum(a: int, b: int) -> str:  # говорим FastAPI, что нужно проверить тип вводимых чисел
    return f'{a} + {b} = {a + b}'


@app.get('/multiply/{num}/{deg}')  # передача значений в url в {}
def degree(num: int, deg: int):
    return f"{num} ** {deg} = {num ** deg}"

@app.post('/user')
def print_name(name: str):
    return {"message": f"hello, {name}"}

@app.get('/booking/all', response_model=List[BookingGet]) # List  - тип возвращаемого response_model элемента список,
                                                        # где все элементы BookingGet
def all_address():
    conn = psycopg2.connect("postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
                            cursor_factory=RealDictCursor) # наследуемся от класса для превращения ответа БД в словарь(dict)
    cursor = conn.cursor()
    cursor.execute(
        """
    SELECT  bookid as "id",
            facid as "facility_id",
            memid as "member_id",
            starttime as "start_time",
            slots
    FROM bookings
        """
    )
    result = cursor.fetchall()
    #logger.info(result) # логирование из биб-ки loguru
    return result

@app.post('/user/validate') # принимаем json из body в формате указанном в SimpleUser и валидируем по нему
def validate_user(user: SimpleUser):
    logger.info(user.dict())
    return {'message' : f' Hi, {user.first_name}, validation compleate' }

@app.get('/error/{num}')
def show_error(num: int):
    if num == 501:
        raise HTTPException(501, 'Test Error 501') # при наличии условий, выводим определенную ошибку
    elif num == 400:
        raise HTTPException(400, 'Test Error 400 users' )
    else:
        return 'Not Error'