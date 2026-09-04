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