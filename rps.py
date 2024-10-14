# Write a program that plays the game of 'rock', 'paper', 'scissors'

'''
Input example:
  choose between 'rock', 'paper', 'scissors'

Output example:
  Player choice: 'rock'

 Computer choice: 'paper'
 Computer wins!
'''

# Requirments

# The program must ensure the user only insert accepted values. If a wrong value is 
# inserted, a message should be returned and the user should be asked to insert a value again.

# The computer must choose rock, paper, scissors randomly. Hint: check the random library

import tkinter as tk
from tkinter import messagebox
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "Player wins!"
    else:
        return "Computer wins!"

# Function to handle the player's choice
def play_game(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    
    result_message = f"Player choice: '{player_choice}'\nComputer choice: '{computer_choice}'\n\n{result}"
    messagebox.showinfo("Result", result_message)

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Set dark mode colors
bg_color = "#2E2E2E"
fg_color = "#FFFFFF"
button_bg_color = "#3E3E3E"
button_fg_color = "#FFFFFF"

# Configure the main window for dark mode
root.configure(bg=bg_color)

# Add a label to the window
label = tk.Label(root, text="Choose between 'rock', 'paper', 'scissors':", font=("Helvetica", 16), bg=bg_color, fg=fg_color)
label.pack(pady=20)

# Add buttons for rock, paper, and scissors
rock_button = tk.Button(root, text="Rock", font=("Helvetica", 14), bg=button_bg_color, fg=button_fg_color, command=lambda: play_game('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Helvetica", 14), bg=button_bg_color, fg=button_fg_color, command=lambda: play_game('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Helvetica", 14), bg=button_bg_color, fg=button_fg_color, command=lambda: play_game('scissors'))
scissors_button.pack(pady=5)

# Run the main loop
root.mainloop()
