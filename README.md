# Project: Hangman

## Contents:
1. Milestone 2: Create the variables for the game
    - Define list of words
    - Ask for user input
    - Validate input
2. Milestone 3: Create functions to run checks
    - check_guess: Function to check whether chosen letter exists in word
    - ask_for_input: Function to request and validate input. Single letter is valid input.
3. Milestone 4: Create the Hangman class
    - check_guess: Method to check whether guess exists in chosen word. Inserts correct letter into word and reduces lives for incorrect guess.
    - ask_for_input: Method to request and validate input. Iteratively requests further input if not valid.
4. Milestone 5: Bringing everything together to create Hangman game
    - get_index_all: Additional method added to replace all letters in word_guessed when letter guessed occurs more than once in the word.
    - play_game: Function created to bring all methods together to allow player to play Hangman. The while loop allows game to continue until player loses all lives or guesses the word correctly.