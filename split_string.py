 # Write a program to split a given string on hyphens and display each substring

 '''
 Input 
  Str1 = "Emma-is-a-data-scientist"

 output must have each sub-string on a new line
 '''

def split(input_str):
  
  # Split the string on hyphens
 substrings = input_str.split('-')

 # Display each substring on a new line
 for substring in substrings:
  print(substring)

# Input string
str1 = "Emma-is-a-data-scientist"

# Call the function with the input string
split(str1)