# app/api.py
from fastapi import FastAPI
from app.models import PowRequest, FibonacciRequest, FactorialRequest, OperationResponse
from app.calculator import calculate_pow, calculate_fibonacci, calculate_factorial
from app.db import init_db, save_operation
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)
app = FastAPI(title="MathOps Service")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/pow", response_model=OperationResponse)
def pow_op(req: PowRequest):
    result = calculate_pow(req.x, req.y)
    logger.info(f"POW called with x={req.x}, y={req.y} -> result={result}")
    save_operation("pow", f"x={req.x},y={req.y}", result)
    return {"result": result}

# … celelalte endpoint-uri la fel …
@app.post("/fibonacci", response_model=OperationResponse)
def fibonacci_op(req: FibonacciRequest):
    result = calculate_fibonacci(req.n)
    logger.info(f"FIB called with n={req.n} -> result={result}")
    save_operation("fibonacci", f"n={req.n}", result)
    return {"result": result}

@app.post("/factorial", response_model=OperationResponse)
def factorial_op(req: FactorialRequest):
    result = calculate_factorial(req.n)
    logger.info(f"FACTORIAL called with n={req.n} -> result={result}")
    save_operation("factorial", f"n={req.n}", result)
    return {"result": result}