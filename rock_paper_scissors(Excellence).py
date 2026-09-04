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

def game_start():
    while True:
        user_name = input("Please enter your name: ")
        if user_name == "":
            break
        print("Invalid input. Your name cannot be empty.")

    total_rounds = get_total_rounds()
    player_score = 0
    computer_score = 0
    draw_count = 0

    print(f"Hello {user_name}, starting a {total_rounds} game")

    for current_round in range(1, total_rounds + 1):
        print(f"\n--- Round {current_round} of {total_rounds}")
        player_decided = get_player_choice()
        computer_decided = random.choice(game_choices)
        print(f"{user_name} picked: {player_decided}")
        print(f"Computer picked: {computer_decided}")
        winner = determine_round_winner(player_decided,computer_decided)
        if winner == "player":
            player_score += 1
            print(f"Round Result: {user_name} wins!")
        elif winner == "computer":
            computer_score += 1
            print("Round Result: Computer wins!")
        else:
            draw_count += 1
            print("Round Result: It's a draw!")

        print(
            f"Current Score - "
            f"{user_name}: {player_score} | "
            f"Computer: {computer_score} | "
            f"Draws: {draw_count}"
        )