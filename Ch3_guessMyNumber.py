#franck
#Guess My Number

#the computer picks a random number between 1 and 100
#the player tries to guess it and the computer lets the player know if its hight or low
#or right on the money


#the computer picks a random number between 1 and 100

import random

number = random.randint(1, 100)

print("Guess the number the computer picked:")
chosen_number = int(input("what number do you choose?"))
guesses = 1
while chosen_number is not number:
    if chosen_number < number:
        print("the number you chose is too small ")
    else:
        print("the number you chose is too big")

    chosen_number = int(input("choose another number!:"))
    guesses += 1
print("Congratulation you chose the right number!", number)
print("It took you,", guesses, "tries!")

input("\n\nPress enter to exit.")






