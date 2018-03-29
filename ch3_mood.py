#franck 12/3/2018
#mood computer
#demonstrate the elif clause

import random

print("I sense your energy, your true emotion are coming across the screen.")
print("You are")

mood = random.randint(1,3)

if mood == 1:
    #happy
    print("you are happy")

elif mood == 2:
    #neutral
    print("you are neutral")

elif mood == 3:
    #sed
    print("you are sad")
else:
    print("illegal mood value")

input("\nPress enter to exit.")