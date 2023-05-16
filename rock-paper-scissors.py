# Import the 'os' module to clear the console screen
import os  
import random

# Define constants for the game images
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list of the game images for easy access
GAME_IMAGES = [ROCK, PAPER, SCISSORS]

def get_user_choice():
    """Asks the user to choose an option and returns their choice"""
    print("What do you choose?")
    for i, option in enumerate(["Rock", "Paper", "Scissors"]):
# Display the options available to the user
        print(f"{i}: {option}")  
    while True:
        try:
# Get the user's input            
            user_choice = int(input())  
# Check if the input is valid            
            if 0 <= user_choice <= 2:  
                return user_choice
            else:
                print("Invalid input. Please choose a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please choose a number between 0 and 2.")

# Main game loop
while True:
# Clear the console screen    
    os.system('cls' if os.name == 'nt' else 'clear')  
# Get the user's choice
    user_choice = get_user_choice()  
# Display the user's choice    
    print(GAME_IMAGES[user_choice])  
# Generate a random computer choice
    computer_choice = random.randint(0, 2) 
    print("Computer chose:")
# Display the computer's choice    
    print(GAME_IMAGES[computer_choice])  

# Determine the winner based on the user and computer choices
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n) ")
# Ask the user if they want to play again    
    if play_again.lower() != "y":  
# Exit the game loop if the user doesn't want to play again        
        break  
