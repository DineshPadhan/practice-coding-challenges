# Daily Coding Challenge - 2025-01-31

**Question #29:** Write a Python program to find the highest and lowest values in a list.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:40:52

## Code Preview
```python
def find_highest_lowest(numbers):
    if not numbers:
        return None, None  # Handle empty list case
    highest = numbers[0]
    lowest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return highest, lowest

# Example usage:
number_list = [3, 1, 4, 1, 5, 9, 2, 6]
highest, lowest = find_highest_lowest(number_list)
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

#Example of empty list
empty_list = []
highest, lowest = find_highest_lowest(empty_list)
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
```
