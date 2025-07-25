# Question: Write a Python program to check if a string is a palindrome.
# Date: 2025-07-18
# Question #4
# Generated by Gemini AI

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