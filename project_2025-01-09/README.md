# Daily Coding Challenge - 2025-01-09

**Question #7:** Write a Python program to find the largest number in a list.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:38:35

## Code Preview
```python
def findLargest(numbers):
    if not numbers:
        return None  # Handle empty list case
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage:
numberList = [10, 5, 20, 15, 30, 25]
largestNumber = findLargest(numberList)
print(f"The largest number in the list is: {largestNumber}")

numberList = []
largestNumber = findLargest(numberList)
print(f"The largest number in the list is: {largestNumber}")
```
