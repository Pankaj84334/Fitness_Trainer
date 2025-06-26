from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MathInput(BaseModel):
    a: int
    b: int

@app.post("/add")
def add(data: MathInput):
    return {"result": f"Math Response: {data.a + data.b}"}

@app.post("/subtract")
def subtract(data: MathInput):
    return {"result": f"Math Response: {data.a - data.b}"}

@app.post("/multiply")
def multiply(data: MathInput):
    return {"result": f"Math Response: {data.a * data.b}"}

@app.post("/divide")
def divide(data: MathInput):
    if data.b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": f"Math Response: {data.a / data.b}"}
