#franck 1/05/2018
#Constructor Critter
# Demonstrate constructors

class Critter(object):
    """A virtual pet"""
    def __init__(self):
        print("a new critter has been born!")

    def talk(self):
        print("\nHi. I'am an instance of class critter.")

#main

crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit.")
