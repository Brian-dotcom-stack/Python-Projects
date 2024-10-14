# Print a staircase

'''Write a script that given an integer, print a staircase made of numvbers

  Hint: Nest for loops
'''

# Define the number of stepes for the staircase

num = 7

# Outer loop for each step

for i in range(1, num + 1):
 
 # Inner loop for printing numbers
 for j in range(1, i + 1):
  print(j, end=" ")

 print() 