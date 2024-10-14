# COUNT LETTERS DIGIT AND SPECIAL SYMBOLS:

# Write a program that count all letters, digits and symbol from a given string:

""" 
Input: "P@#yn26at^&i5ve"

Output: 
Chars = 8
Digits = 3
Symbols = 4
"""

def count_chars_digits_symbols(input_str):
 chars = 0
 digits = 0
 symbols = 0

 for ch in input_str:
  if ch.isalpha():
   chars += 1
  elif ch.isdigit():
   digits += 1
  else: 
   symbols += 1
 
 return chars, digits, symbols

# Input string

Input: "P@#yn26at^&i5ve"

# Get the counts

chars, digits, symbols = count_chars_digits_symbols(input_str)


# Print the counts

print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}" )