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