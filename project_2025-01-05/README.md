# Daily Coding Challenge - 2025-01-05

**Question #3:** Write a Python program to find the factorial of a number.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:38:13

## Code Preview
```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

```
