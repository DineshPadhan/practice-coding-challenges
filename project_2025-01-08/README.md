# Daily Coding Challenge - 2025-01-08

**Question #6:** Write a Python program to count vowels in a string.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:38:29

## Code Preview
```python
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Example usage
string = "Hello, World!"
number_of_vowels = count_vowels(string)
print(f"The number of vowels in the string is: {number_of_vowels}")
```
