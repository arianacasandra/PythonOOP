from math import pow as math_pow

def calculate_pow(x: float, y: float) -> float:
    return math_pow(x, y)

def calculate_fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)


