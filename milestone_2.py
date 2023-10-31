#Hangman Project

import random

#Milestone 2
##Task 1: Define list of words
word_list = ["apple","pear","kiwi","cherries","blueberries"]
print(word_list)

##Task 2: Randomly choose word
word = random.choice(word_list)
print(word)

##Task 3: Request user input
guess = input("Enter a letter ")

##Task 4: Input validation
def check_letter(x):
    if len(x) == 1 and x.isnumeric() == False:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

check_letter(guess)