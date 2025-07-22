# Daily Coding Challenge - 2025-01-19

**Question #17:** Write a Python program to find the GCD of two numbers.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:39:32

## Code Preview
```python
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
```
