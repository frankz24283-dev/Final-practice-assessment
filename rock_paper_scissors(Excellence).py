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

def get_valid_player_name(): #Get the user name, and make sure they don't enter what I don't want. check the name
    while True:
        name = input("Please enter your name: ")
        if len(name) > 0 :
            return name
        print("Invalid input! Name can not be empty. Please try again. \n")

def get_valid_rounds(): #Retrieve and verify the number of game rounds, and handle invalid data types (such as letters and null values) and boundary ranges.
    while True:
        questions_ask_user = f"How many rounds would you like to play ({MIN_ROUNDS- MAX_ROUNDS})"
        user_input = input(questions_ask_user)

        if not user_input.isdigit(): #Check if the input consists entirely of numbers and block non-numeric characters.
            print("Invalid imput! Please enter a valid positive integer. \n")
            countine
        rounds = int(user_input)

        if MIN_ROUNDS <= rounds <= MAX_ROUNDS:
            return rounds
        else:
            print(f"Out of range! Please enter a number between {MIN_ROUNDS} and {MAX_ROUNDS}")
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ")
        if choice == "rock" or choice == "paper" or choice == "scissors":
            return choice
        else:
            print("Invalid choice! Please type rock, paper, or scissors.\n")
def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(player_choice, computer_choice):
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
def showing_final_result(name,player_score, computer_score, draws):
    print(f"{name}'s score: {player_score}")
    print(f"Computer's score: {computer_score}")
    print(f"Draws: {draws}")

    if player_score > computer_score:
        print(f"\nCongratulations {name}! You won the game!")
    elif computer_score > player_score:
        print("\nThe computer won the game!")
    else:
        print("\nThe game ended in a draw!")

def play_game():
    name = get_valid_player_name()
    rounds = get_valid_rounds()
    player_score = 0
    computer_score = 0
    draws = 0

    print(f"\nWelcome, {name}!")
    print(f"You are going to play {rounds} round(s).\n")

    for round_number in range(1, rounds + 1):
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)