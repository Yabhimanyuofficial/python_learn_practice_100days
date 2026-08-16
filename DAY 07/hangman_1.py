import random
# TODO-5.1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import stages, logo

# TODO-4.1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.
lives = 6
# TODO-5.3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# TODO-1.1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
#print(chosen_word)

# TODO-2.1: Create a "placeholder" with the same number of blanks as the chosen_word. So if the chosen_word was "apple", the display should be "_ _ _ _ _". Hint: You can use a loop to do this.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print("Word to guess: " + placeholder)

# TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and displayed them.
game_over = False
correct_letters = []

while not game_over:
    # TODO-5.6: - Update the code below to tell the user how many lives they have left.
    print(f"{lives}/6 LIVES LEFT")
# TODO-1.2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    # TODO-2.2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    # TODO-5.4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""
    # TODO-3.2: Change the for loop so that you keep the previous correct letters in display.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "
    print("Word to guess: " + display)

    # TODO-4.2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    # TODO-5.5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            # TODO 5.7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"IT WAS {chosen_word}! YOU LOSE")

    if "_ " not in display:
        game_over = True
        print("You win!")

     # TODO-5.2: - Update the code below to use the stages List from the file hangman_art.py    
    print(stages[lives])


    '''
# TODO-1.3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        '''