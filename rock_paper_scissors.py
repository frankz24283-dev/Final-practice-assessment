'''
  Author: Frank Zhang
  date:27/08/2026
  version:1.0
  descirption: The game of rock paper scissors
'''
import random
choices = ["Rock", "Paper", "Scissors"]
def check_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"
player_name = str(input("Enter your name: "))