import random
#Task 1: Create Hangman Class
## class defintion
class Hangman:

    #class constructor
    def __init__(self,word_list,num_lives = 5):

        #attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_','_','_','_','_']
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    #method to check player guess
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
            for i in self.word:
                if i == guess:
                    self.word_guessed[num_lives-5] = guess
            num_letters -= 1
        else:
            num_lives -= 1
            print("Sorry, " + guess + " is not in the word.")
            print("You have" + num_lives + " left.")

    #method defining input request
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
