from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sum_two(a: int, b: int) -> int:
    return a + b
