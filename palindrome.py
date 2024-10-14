# Write a program that checks if a word is a palindrome

'''
A palindrome is a 
'''

def is_palindrome(word):
 return word == word[::-1]
 
word = 'anna'

if is_palindrome(word):
 print(f"{word} is palindrome")
else:
 print(f"{word} is not palindrome")