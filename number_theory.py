"""Small, independently testable number theory utilities."""
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2: return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0: return False
    return True

def gcd_euclid(a: int, b: int) -> int:
    while b: a, b = b, a % b
    return abs(a)

def fibonacci(n: int) -> int:
    if n < 0: raise ValueError('n must be nonnegative')
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
