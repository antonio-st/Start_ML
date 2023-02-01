from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

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
