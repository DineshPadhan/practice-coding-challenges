# Daily Coding Challenge - 2025-01-29

**Question #27:** Write a Python program to sum all elements of a list.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:40:39

## Code Preview
```python
def sum_list(data):
  """Calculate the sum of elements in a list.

  Args:
    data: A list of numbers.

  Returns:
    The sum of all elements in the list. Returns 0 for an empty list.
  """
  if not data:
    return 0
  total = 0
  for number in data:
    total += number
  return total

```
