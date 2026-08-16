from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_number(user_guess, actual_number, turns):
    ''' Checks number against guess. Returns the number of turns remaining. '''
    if user_guess > actual_number:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The number was {actual_number}.")
        

# Function to set the difficulty of the game
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    print(f"Pssst, the correct answer is {number}")


    turns = set_difficulty()
    

    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
    # Let the user guess a number.
        guess = int(input("Make a guess: "))
        
        turns = check_number(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")

game()

    # track the number of turns and reduce by 1 if they get it wrong.


