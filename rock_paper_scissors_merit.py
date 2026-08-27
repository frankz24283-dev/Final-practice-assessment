'''
  Author: Frank Zhang
  date:28/08/2026
  version:2.0
  descirption: The game of rock paper scissors
'''
import random
game_choices = ["rock","paper", "scissors"]
def determine_round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"

    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    return "computer"
def get_total_rounds():
    while True:
        number_rounds = int(input("How many rounds would you like to play (1-10)? "))
        if 1 <= number_rounds <= 10:
            return number_rounds
        else:
            print("Please enter a number between 1 and 10.")