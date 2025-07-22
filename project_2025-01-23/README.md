# Daily Coding Challenge - 2025-01-23

**Question #21:** Write a Python program to count the number of occurrences of each character in a string.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:40:04

## Code Preview
```python
def count_char_occurrences(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

# Example usage:
input_string = "hello world"
result = count_char_occurrences(input_string)
print(result)
```
