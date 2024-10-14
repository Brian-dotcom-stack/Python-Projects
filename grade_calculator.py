# mod 2 homework

# write a program that takes two numbers, checks which one is the biggest and return a message.

# output should tell the biggest number or if the numbers are equal
# make it dynamic
# implement exception handling

# try: Contains the main logic for prompting user input and comparing the numbers.

try:

    # prompt user for two numbers
 
    num1 = int(input("What is the first number: "))
    num2 = int(input("Now enter the second number: "))

# except ValueError: handle the case where the input is not an integer, providing a specific error message.

except ValueError: 
    print("Error: Invalid input, please enter a number")

# else: runs if no exceptions occur in the try block
else:
 
    # determine which number is the biggest or if they are equal

    if num1 > num2:
        print(f"{num1} is the biggest number")
    elif num1 < num2:
        print(f"{num2} is the biggest number")
    else:
        print("The numbers are both equal") 

    # indicate that no error occurred
    print("No errors occurred.")

# finally: runs no matter what, can be used to clean up resources if needed

finally:
    print("Execution complete.")



# write a program that is going to give the grade of a student according to the score obtained

# if, elif, else 

# score >= 90: 'A' 80 <= score >= 89: 'B' 70 <= score <= 79: 'C' 60 <= score <= 69: 'D' score < 59: 'F' score

score_obtained = int(input("Enter the score: "))

if score_obtained >= 90: 
 print("A")
elif score_obtained >= 80 and score_obtained <= 89:
    print("B")
elif score_obtained >= 70 and score_obtained <= 79:
    print("C")
elif score_obtained >= 60 and score_obtained <= 69:
 print("D")  
else: 
 print("F")  
 

# write a program that given a number, it will play the fizz buzz game

# check what the modulo operator does
# check for loops and the range() function

# A Modulo is a binary operator that calculates the remainder of the division between two numbers

a = 5
b = 2

modulo = a % b
print(modulo)

# loops in python are used to execute a block of code repeatedly until a certain condition is met

# for loops in python are used to iterate over a sequence of lists, strings, set, dictionaries or tuples

# for variable in sequence:

# iterate over a list of fruits

fruits = ["banana", "apple", "orange"]

for fruit in fruits:
 print(fruits)


# iterating over a range of numbers

for i in range(11):
 if i < 5:
  print(i)


# a while loop is used repeatedly to execute a block of code until a certain condition is met.

count = 0 

while count < 10:
 print(count)
 count += 1


# write a program that given a number, it will play the fizz buzz game

# check what the modulo operator does
# check for loops and the range() function


# for loop iterates over each number from 1 to 20

for i in range(1, 20):
 
# check for multiples of 3 and 5

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

# this codition checks if the number 'i' is divisible by 3
    elif i % 3 == 0:
        print("Fizz")

# this condition checks if the number 'i' is divisible by 5
    elif i % 5 == 0:
        print("Buzz")

# print the number number if none of the conditions are met

    else:
        print(i)



# Create a program that asks the user to guess the number that has been randomly generated.
# The user should be able to try continuously until they find the correct number.
# The program should stop as soon as the number is found.

# At each iteration the program should tell the user if the number is too high or too low or the correct number one.
# Implement a way to assign only 5 attempts to the user. Each iteration should show the attempt left.


import random

# Define guess the number function

def guess_number():

# Generate a random number from 1 to 100

    random_number = random.randint(1, 100)
    attempts = 5

    print("Guess a number between 1 and 100. You have 5 attempts.")

    for attempt in range(attempts, 0, -1):
        print(f"Attempts left: {attempts}") 

        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Check if the guess is correct
        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            return
        
        # If its the last attempt and the guess is incorrect
        elif attempt == 1:
            break

        elif user_guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again!")

        # Decrease the number of attempts

        attempts -= 1

    # If all the attempts are used
    print(f"You have run out of attempts. The number is: {random_number}")

# Run the guessing game

guess_number()