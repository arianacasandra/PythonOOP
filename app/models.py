from pydantic import BaseModel

class PowRequest(BaseModel):
    x: float
    y: float

class FibonacciRequest(BaseModel):
    n: int

class FactorialRequest(BaseModel):
    n: int

class OperationResponse(BaseModel):
    result: float | int
