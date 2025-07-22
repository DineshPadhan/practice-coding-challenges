# Daily Coding Challenge - 2025-07-18

**Question #4:** Write a Python program to check if a string is a palindrome.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-18 00:00:04

## Code Preview
```python
def is_palindrome(text):
    processed_text = ''.join(filter(str.isalnum, text)).lower()
    return processed_text == processed_text[::-1]

# Example usage:
string1 = "racecar"
string2 = "A man, a plan, a canal: Panama"
string3 = "hello"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")
```
