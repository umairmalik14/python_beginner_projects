# Ask the user to make a choice
# If choice is not valid 
#   Print an Error 
# Let the computer to make a choice
# Print choice (Emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
# Terminate

import random

emojis = {'r': "ROCK", 'p': 'PAPER', 's': 'SCISSORS'}
choices = ('r', 'p', 's')

def get_user_choice():
    while True: 
        user_choice = input("Rock, Paper, Scissors (r/p/s): ").lower() 
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")
            

def display_choice(user_choice, computer_choices):
    print(f"you chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choices]}")

def determin_winner(user_choice, computer_choices):
    if user_choice == computer_choices:
        print('Tie!')
    elif(
        (user_choice == 'r' and computer_choices == 's') or 
        (user_choice == 's' and computer_choices == 'p') or 
        (user_choice == 'p' and computer_choices == 'r')):
        print('You Win')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice =  get_user_choice()

        computer_choices = random.choice(choices) 

        display_choice(user_choice, computer_choices)
        determin_winner(user_choice, computer_choices)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break


play_game()