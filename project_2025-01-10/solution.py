# Question: Write a Python program to sort a list of numbers in ascending order.
# Date: 2025-01-10
# Question #8
# Generated by Gemini AI

def sort_numbers(numbers):
  """Sorts a list of numbers in ascending order.

  Args:
    numbers: A list of numbers.

  Returns:
    A new list containing the numbers sorted in ascending order.
  """
  return sorted(numbers)

# Example usage
unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sort_numbers(unsorted_numbers)
print(f"Original list: {unsorted_numbers}")
print(f"Sorted list: {sorted_numbers}")