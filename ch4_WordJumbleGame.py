#franck
#02/042018

#Word Jumble
#
#The comupter picks a random word and then jumbles it
#The player has to guess the original word

import random

#create a sequence of words to chose from

WORDS = ("python", "jumble", "vancouver", "mila", "answer", "pasta" , "lazy")

#Computer pick one randomly from the sequence(tuple)
word = random.choice(WORDS)

#Create a variable to use later to see if the guess is correct
correct = word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position +1):]


# Start the game
print(
"""
        Welcome to Word Jumble!
    Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("the Jumble is:", jumble)

guess = input("\nYour guess:")
while guess != correct and guess != "":
    print("Sorry, thats's not it.")
    guess = input("your guess: ")

    if guess == correct:
        print("that it you won the game!\n")
print("thanks for playing")

input("\n\nPress enter to exit.")
