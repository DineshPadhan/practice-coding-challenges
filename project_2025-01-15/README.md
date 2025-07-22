# Daily Coding Challenge - 2025-01-15

**Question #13:** Write a Python program to merge two dictionaries.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:39:07

## Code Preview
```python
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
