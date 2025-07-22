# Daily Coding Challenge - 2025-07-16

**Question #2:** Write a Python program to check if a number is prime.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-16 00:00:04

## Code Preview
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
```
