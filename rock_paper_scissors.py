'''
  Author: Frank Zhang
  date:27/08/2026
  version:1.0
  descirption: The game of rock paper scissors
'''
import random
choices = ["rock", "paper", "scissors"]
def check_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"
player_name = str(input("Enter your name: "))
rounds = int(input("How many rounds would you like to play (1-10)? "))
player_score = 0
computer_score = 0
for i in range(rounds):
    print("\nRound", i + 1)
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_descide = random.choice(choices)
    print("Computer chose: ", computer_descide)
    result = check_winner(player_choice, computer_descide)