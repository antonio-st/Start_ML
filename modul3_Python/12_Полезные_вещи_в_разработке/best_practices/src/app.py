import psycopg2
import uvicorn
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection
from fastapi import FastAPI, Depends
import os  # для считывания переменных окружения bash .env при подключении к БД
from dotenv import load_dotenv  # для считывания переменных .env
import yaml  # для открытия файла конфигурации params.yaml
from pathlib import Path  # модуль для определения пути к папке
from src.crud import get_feed, get_likes

app = FastAPI()

# вызываем переменные .env
load_dotenv()


def get_db():
    with psycopg2.connect(
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT"),
            database=os.environ.get("POSTGRES_DATABASE"),
    ) as db:
        return db


# конфиг, путь определяем с Path
def config():
    with open(Path(__file__).parent.parent / "params.yaml", "r") as f:
        return yaml.safe_load(f)  # вернет словарь (в нашем случае один ключ: значение)


@app.get("/user")
def get_all_users(limit: int = 5, db: connection = Depends(get_db)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            """
            SELECT * 
            FROM "user"
            LIMIT %(limit)s
            """,
            {"limit": limit},  # вместо f-строки, передаем параметры через второй аргумент метода execute
            #  - параметры передаются при помощи словаря и подставляются в запрос.
        )
        return cursor.fetchall()


@app.get("/user/feed")
def get_user_feed(user_id: int = 200, limit: int = 5, db: connection = Depends(get_db), config: dict = Depends(config)):
    return get_feed(user_id, limit, db, config)


@app.get("/user/likes")
def get_feed_likes(user_id: int = 200, limit: int = 5, db: connection = Depends(get_db), config: dict = Depends(config)):
    return get_likes(user_id, limit, db, config)

if __name__ == '__main__':
    load_dotenv()
    # uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)
    uvicorn.run("app:app", reload=True)
