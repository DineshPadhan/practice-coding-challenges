# Daily Coding Challenge - 2025-07-21

**Question #7:** Write a Python program to find the largest number in a list.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-21 00:00:04

## Code Preview
```python
def find_largest_number(numbers):
    if not numbers:
        return None  # Handle empty list case
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number

# Get input from the user
number_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in number_str.split()]

# Find and print the largest number
largest = find_largest_number(numbers)
if largest is not None:
    print("The largest number is:", largest)
else:
    print("The list is empty.")
```
