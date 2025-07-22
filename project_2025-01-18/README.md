# Daily Coding Challenge - 2025-01-18

**Question #16:** Write a Python program to print the Fibonacci sequence.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:39:24

## Code Preview
```python
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib

number_terms = 10
print(fibonacci_sequence(number_terms))
```
