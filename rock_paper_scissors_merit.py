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

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in game_choices:
            return choice
        else:
            print("Invalid move. Please type rock, paper, or scissors.")

def get_total_rounds():
    while True:
        number_rounds = int(input("How many rounds would you like to play (1-10)? "))
        if 1 <= number_rounds <= 10:
            return number_rounds
        else:
            print("Please enter a number between 1 and 10.")

def game_start():
    user_name = input("Please enter your name: ")
    total_rounds = get_total_rounds()
    player_score = 0
    computer_score = 0
    draw_count = 0
    print(f"\nHello {user_name}, starting a {total_rounds}")

    for current_round in range(1, total_rounds + 1):
        print(f"\n--- Round {current_round} of {total_rounds}")
        player_descided = get_player_choice
        computer_descided = random.choice(game_choices)
        print(f"{user_name} picked: {player_descided}")
        print(f"computer picked: {computer_descided}")