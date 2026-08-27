'''
  Author: Frank Zhang
  date:27/08/2026
  version:1.0
  descirption: The game of rock paper scissors
'''
import random
choices = ["rock", "paper", "scissors"] #Set the list of rock paper scissors, let the user and computer easy to pick
def check_winner(player, computer): #Descided who win the game, check the computer or user win this game
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
    if result == "player":
        print(player_name, "wins this round!")
        player_score = player_score + 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score = computer_score + 1
    else:
        print("It is a draw!")
    print("Score:", player_name, player_score, "-", computer_score, "Computer")
print("\n--- Game Over ---")
print("Final Score:")
print(player_name, ":", player_score)
print("Computer:", computer_score)

if player_score > computer_score:
    print(player_name, "won the game!")
elif computer_score > player_score:
    print("Computer won the game!")
else:
    print("The game is a tie!")