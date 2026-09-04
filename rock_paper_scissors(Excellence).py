'''
    author:Frank Zhang
    date:5/09-2026
    version:3.0
    descirption: The game of rock paper scissors
'''
import random
game_choices = ["rock", "paper", "scissors"]

def determine_round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    if(
        (player_choice == "rock" and computer_choice == "scissors")
        or
        (player_choice == "paper" and computer_choice == "rock")
        or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    return "computer"

def get_player_choice():
    while True:
        choice = input( "Enter your choice (rock, paper, or scissors): ").lower
        if choice == "":
            print("Invalid input. Your choice cannot be empty.")
            continue
        if choice in game_choices:
            return choice
        print("Invalid move. Please type rock, paper, or scissors.")

def get_total_rounds():
    while True:
        user_input = input("How many rounds would you like to play (1-10)? ")
        if user_input == "":
            print("Invalid input. Please enter a number. The input cannot be empty.")
            continue
        if not user_input.isdigit():
            print("Invalid input. Please enter a whole number between 1-10")
            continue

        number_rounds = int(user_input)

        if 1 <= number_rounds <= 10:
            return number_rounds
        print("Out of range. Please enter a number between 1 and 10.")