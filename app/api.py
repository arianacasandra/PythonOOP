# app/api.py
from fastapi import FastAPI
from app.models import PowRequest, FibonacciRequest, FactorialRequest, OperationResponse
from app.calculator import calculate_pow, calculate_fibonacci, calculate_factorial
from app.db import init_db, save_operation

app = FastAPI(title="MathOps Service")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/pow", response_model=OperationResponse)
def pow_op(req: PowRequest):
    result = calculate_pow(req.x, req.y)
    save_operation("pow", f"x={req.x},y={req.y}", result)
    print("mere")   # pentru debug
    return {"result": result}

# … celelalte endpoint-uri la fel …
@app.post("/fibonacci", response_model=OperationResponse)
def fibonacci_op(req: FibonacciRequest):
    result = calculate_fibonacci(req.n)
    save_operation("fibonacci", f"n={req.n}", result)
    return {"result": result}

@app.post("/factorial", response_model=OperationResponse)
def factorial_op(req: FactorialRequest):
    result = calculate_factorial(req.n)
    save_operation("factorial", f"n={req.n}", result)
    return {"result": result}