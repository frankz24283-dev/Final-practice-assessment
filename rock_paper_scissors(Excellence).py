'''
   author:Frank Zhang
   date:29/08/2026
   version:3.0
   descirption: The game of rock paper sicssors
'''
import random
MIN_ROUNDS = 1
MAX_ROUNDS = 10
CHOICES = ["rock", "paper", "scissors"]

def get_valid_player_name(): #Get the user name, and make sure they don't enter what I don't want. check the name
    while True:
        name = input("Please enter your name: ")
        if len(name) > 0 :
            return name
        print("Invalid input! Name can not be empty. Please try again. \n")

def get_valid_rounds(): #Retrieve and verify the number of game rounds, and handle invalid data types (such as letters and null values) and boundary ranges.
    while True:
        questions_ask_user = f"How many rounds would you like to play ({MIN_ROUNDS- MAX_ROUNDS})"
        user_input = input(questions_ask_user)

        if not user_input(): #Check if the input consists entirely of numbers and block non-numeric characters.
            print("Invalid imput! Please enter a valid positive integer. \n")
        rounds = int(user_input)

        if MIN_ROUNDS <= rounds <= MAX_ROUNDS:
            return rounds
        else:
            print(f"Out of range! Please enter a number between {MIN_ROUNDS} and {MAX_ROUNDS}")
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ")
        if choice == "rock" or choice == "paper" or choice == "scissors":
            return choice
        else:
            print("Invalid choice! Please type rock, paper, or scissors.\n")
