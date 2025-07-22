# Daily Coding Challenge - 2025-01-28

**Question #26:** Write a Python program to find the length of a string without using len().

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:40:34

## Code Preview
```python
def find_length(input_string):
    count = 0
    for _ in input_string:
        count += 1
    return count

#Example
string1 = "hello"
print(find_length(string1)) # Output: 5

string2 = "1234567890"
print(find_length(string2)) # Output: 10
```
