# Daily Coding Challenge - 2025-01-27

**Question #25:** Write a Python program to find the sum of digits of a number.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:40:27

## Code Preview
```python
def sum_digits(number):
  sum = 0
  while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
  return sum

number = int(input("Enter a number: "))
result = sum_digits(number)
print("Sum of digits:", result)
```
