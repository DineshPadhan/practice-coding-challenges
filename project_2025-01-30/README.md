# Daily Coding Challenge - 2025-01-30

**Question #28:** Write a Python program to find the average of a list of numbers.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:40:45

## Code Preview
```python
def find_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Get input from the user
number_str = input("Enter numbers separated by spaces: ")
numbers = [float(x) for x in number_str.split()]

# Calculate and print the average
average = find_average(numbers)
print("Average: ", average)
```
