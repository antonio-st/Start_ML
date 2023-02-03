from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


def get_db():
    conn = psycopg2.connect(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
        cursor_factory=RealDictCursor
    )
    return conn


# класс для проверки вход. данных в @app.get("/post/{post_id}"
class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


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
