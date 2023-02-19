from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date

    class Config:
        orm_mode = True


@app.post("/user/validate")
def validation(json_file: User):
    return f'Will add user: {json_file.name} {json_file.surname} with age {json_file.age}'


@app.get("/user/{id}")
def find_user(id: int):
    conn = psycopg2.connect(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
        cursor_factory=RealDictCursor
    )
    cursor = conn.cursor()  # cursor - это объект, который отвечает за взаимодействие с БД

    cursor.execute(
        f"""
        SELECT 
            gender, age, city
        FROM "user"
        WHERE id = {id}
        """)

    results = cursor.fetchone()  # Получаем результаты (fetchall() - "получить всё")
    cursor.close()
    conn.close()
    if not results: # if result == []
        raise HTTPException(404, "user not found")
    return results


