from fastapi import FastAPI
from datetime import timedelta, date

app = FastAPI()


@app.get("/sum_date")
def sum_date(current_date: date, offset: int):
    result = current_date + timedelta(days=offset)
    return result
