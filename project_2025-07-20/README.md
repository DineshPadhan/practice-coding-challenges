# Daily Coding Challenge - 2025-07-20

**Question #6:** Write a Python program to count vowels in a string.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-20 00:00:04

## Code Preview
```python
def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
result = count_vowels(input_string)
print("Number of vowels:", result)
```
