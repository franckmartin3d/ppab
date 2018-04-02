#franck
#02/04/2018
#random access Program
#Demonstrate sting indexing

import random

word = "index"
print("the word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\npress the enter key to exit")

