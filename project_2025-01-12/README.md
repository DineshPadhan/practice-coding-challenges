# Daily Coding Challenge - 2025-01-12

**Question #10:** Write a Python program to remove duplicates from a list.

**Solution:** Check `solution.py` for the Python implementation.

**Generated:** 2025-07-22 15:38:51

## Code Preview
```python
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#Example
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(f"Original list: {my_list}")
print(f"List without duplicates: {unique_list}")
```
