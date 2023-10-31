import random
import re

#Task 1: Create Hangman Class
## class defintion
class Hangman:

    #class constructor
    def __init__(self,word_list,num_lives = 5):

        #attributes
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []

        #initialise attributes
        print("The mistery word has " + str(self.num_letters) + " characters")

    # Method replacing all instances of a correct guess in attribute word_guessed
    def get_index_all(self,guess):
        indices_object = re.finditer(pattern=guess, string=self.word)
        indices = [index.start() for index in indices_object]
        for x in indices:
            self.word_guessed[x] = guess

    # Method to check if player guess exists in the word
    # Updates word_guessed if guess correct and reduces num_lives if guess incorrect
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
            for i in self.word:
                if i == guess:
                    self.get_index_all(guess)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print("Sorry, " + guess + " is not in the word.")
            print("You have " + str(self.num_lives) + " lives left.")
        self.list_of_guesses.append(guess)

    # Method for input request
    # Request and validates input. Runs check_guess method 
    def ask_for_input(self):

        while True:
            guess = input("Guess a letter ")
            if len(guess) > 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break


# Function to play Hangman game
def play_game(word_list):
    num_lives=5
    game = Hangman(word_list, num_lives=5)

    # Loop continues until player wins/ loses all lives
    while True:
        print(game.word_guessed)

        game.ask_for_input()
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

# Game instance
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

