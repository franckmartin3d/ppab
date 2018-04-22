#franck 18/04/2018
#hangman game


# The classic game of Hangman. The computer picks a random word
# and the player wrong to guess it, one letter at a time. If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
import random

#constant hangman TUPLE graphics
###################################graphics#########################################
HANGMAN = (
    """
------
|    |
|
|
|
|
|
|
|
----------
""", """
------
|    |
|    O
|
|
|
|
|
|
----------
""", """
------
|    |
|    O
|   -+-
|
|
|
|
|
----------
""", """
------
|    |
|    O
|  /-+-
|
|
|
|
|
----------
""", """
------
|    |
|    O
|  /-+-/
|
|
|
 |
 |
----------
""", """
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
----------
""", """
------
|    |
|    O
|  /-+-/
|    |
|    |
|    |
|    |
|
----------
""", """
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------
""")

######################################VARIABLE NEEDED######################################

# constant ro represent the maximum number of wrong guess a player can make
MAX_WRONG = len(HANGMAN) -1

#word user can choose
WORDS = ("SNOWBOARD", "HOCKEY", "LAZY", "BED", "UNREAL")

#initialize variable
word = random.choice(WORDS) # the word to be guessed

# what the player has guessed so far in the game
# one dash for each letter in word to be guessed
so_far = "-" * len(word)

#number of wrong guess by user
wrong_guess = 0

#letter player already guessed
#list
letter_used = []

###########################################MAIN LOOP##############################################


print("welcome to Hangman. goodluck!")

while wrong_guess < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong_guess])
    print("\nYou've used the following letters:\n", letter_used)
    print("\nSo far, the word is:\n", so_far)

    ########players guess#############
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in letter_used:
        print("your already guess the letter", guess)
        guess = input("\n\nEnter your guess: ")
        guess =guess.upper()

    # add letter to letter used list
    letter_used.append(guess)


    ###########checking guess###########################################

    if guess in word:
        print("Yes!", guess, "is in the word!")

        # creat a new so_far to include guess
        new = " "
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry the letter", guess, "is not in the word.")
        wrong_guess += 1

############################## ending the game ###############
if wrong_guess == MAX_WRONG:
    print(HANGMAN[wrong_guess])
    print("\n you've been hanged!")

else:
    print("\nCONGRATULATION YOU GUESS IT")

print("\nThe word was", word)
input("\n\nPress the enter key to exit.")






