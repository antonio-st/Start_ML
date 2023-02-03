from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import date
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# функция подключения к БД для механизма dependency injection
def get_db():
    conn = psycopg2.connect(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
        cursor_factory=RealDictCursor
    )
    return conn

# валидация для @app.post("/user/validate")
class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date

    class Config:
        orm_mode = True

# валидация для @app.get("/post/{post_id}"
class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


@app.post("/user/validate")
def validation(json_file: User):
    return f'Will add user: {json_file.name} {json_file.surname} with age {json_file.age}'

# получение пола, возраста и города из user по id
@app.get("/user/{id}")
def find_user(id: int, db=Depends(get_db)):
    cursor = db.cursor()  # cursor - это объект, который отвечает за взаимодействие с БД
    cursor.execute(
        f"""
        SELECT 
            gender, age, city
        FROM "user"
        WHERE id = {id}
        """)
    results = cursor.fetchone()  # Получаем результаты (fetchall() - "получить всё")
    if not results: # if result == []
        raise HTTPException(404, "user not found")
    return results
    cursor.close()
    db.conn.close()

# получение id, текста и темы из post
@app.get("/post/{id}", response_model=PostResponse)
def find_user(id: int, db=Depends(get_db)) -> PostResponse:
    cursor = db.cursor()
    cursor.execute(
        f"""
        SELECT 
            id, text, topic
        FROM "post"
        WHERE id = {id}
        """)
    results = cursor.fetchone()

    if not results:
        raise HTTPException(404, f"post {id} not found")
    return PostResponse(**results)
    cursor.close()
    conn.close()