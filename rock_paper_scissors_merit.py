'''
  Author: Frank Zhang
  date:28/08/2026
  version:2.0
  descirption: The game of rock paper scissors
'''
import random
game_choices = ["rock","paper", "scissors"] #Avaiable list for user to choose, rock paper or scissors

def determine_round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"

    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "player" #Check all three possiable results for player to win the game
    return "computer"

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower() #Get the user to choices what they want
        if choice in game_choices:
            return choice
        else:
            print("Invalid move. Please type rock, paper, or scissors.")
# Get and verify the total number of games the player wants to play (within the range of 1 to 10).
def get_total_rounds():
    while True:
        number_rounds = int(input("How many rounds would you like to play (1-10)? ")) #Boundary check if the number between the 1-10.
        if 1 <= number_rounds <= 10:
            return number_rounds
        else:
            print("Please enter a number between 1 and 10.")
#Main game start 
def game_start():
    user_name = input("Please enter your name: ")
    #Obtain the total number of games within the valid range
    total_rounds = get_total_rounds()
    #Record the scores of both sides and the number of ties.
    player_score = 0
    computer_score = 0
    draw_count = 0
    print(f"\nHello {user_name}, starting a {total_rounds}")
# The main game loops, proceeding in turns according to the specified number of rounds.
    for current_round in range(1, total_rounds + 1):
        print(f"\n--- Round {current_round} of {total_rounds}")
        # Obtaining a choice from both parties
        player_descided = get_player_choice()
        computer_descided = random.choice(game_choices)
        print(f"{user_name} picked: {player_descided}")
        print(f"computer picked: {computer_descided}")
# Determine the authorities' decision and update the score
        winner = determine_round_winner(player_descided, computer_descided)
        if winner =="player":
            player_score += 1
            print(f"Round Result: {user_name} wins!")
        elif winner == "computer":
            computer_score += 1
            print("Round Result: Computer wins!")
        else:
            draw_count += 1
            print("Round Result: It's a draw!, goot job on you guys")
# Output the cumulative score after the end of the current round.
        print(f"Current score{user_name}: {player_score} | Computer: {computer_score} | Draws: {draw_count}")
# Output a summary and feedback after the game ends
    print(f"Total Rounds Played: {total_rounds}")
    print(f"{user_name}: {player_score} | Computer: {computer_score} | Draws: {draw_count}")
    if player_score > computer_score:
        print(f"Congratulations {user_name}! You won this game")
    elif computer_score > player_score:
        print(f"Computer won the game, the user need some hard work")
    else:
        print(f"The game end with draw")
game_start()