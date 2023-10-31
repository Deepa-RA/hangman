import random
#Milestone 2
# Task 1: Define list of words
word_list = ["apple","pear","kiwi","cherries","blueberries"]

#Task 2: Randomly choose word
word = random.choice(word_list)
print(word)

#Milestone 3

# Ask for input
guess = input("Guess a letter ")

# Task 2
## Check if letter is in randomly selected word
def check_guess(x):
    x = x.lower()
    if x in word:
        print("Good guess! " + x + " is in the word.")
    else:
        print("Sorry, " + x + " is not in the word. Try again.")

##Iteratively check if the input is a valid guess
def ask_for_input(x):
    while len(x) > 1 or x.isalpha() == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
        x = input("Guess a letter ")
    check_guess(x)

ask_for_input(guess)



 







