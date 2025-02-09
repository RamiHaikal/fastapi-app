from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}

class SumRequest(BaseModel):
    a: int
    b: int

@app.post("/sum")
def calculate_sum(request: SumRequest):

    total = request.a + request.b
    return {"sum": total}