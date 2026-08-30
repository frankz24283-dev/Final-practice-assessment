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

def get_valid_player_name():
    while True:
        name = input("Please enter your name: ")
        if len(name) > 0 :
            return name
        print("Invalid input! Name can not be empty. Please try again. \n")

def get_valid_rounds():
    while True:
        questions_ask_user = f"How many rounds would you like to play ({MIN_ROUNDS- MAX_ROUNDS})"
        user_input = input(questions_ask_user)

        if not user_input():
            print("Invalid imput! Please enter a valid positive integer. \n")
        rounds = int(user_input)

        if MIN_ROUNDS <= rounds <= MAX_ROUNDS:
            return rounds
        else:
            print(f"Out of range! Please enter a number between {MIN_ROUNDS} and {MAX_ROUNDS}")
