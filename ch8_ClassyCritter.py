#franck 1/05/2018
#Classy Critter
# Demonstrate class attributes and static methods

class Critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("\nThe total number of critter is" , Critter.total)

    def __init__(self, name):
        print("A critter is born!")
        self.name = name
        Critter.total += 1

#main
print("Accessing the class attribute Critter.total:", end= " ")
print(Critter.total)

print("\nCreating critters.")
crit1 = Critter("Critter 1")
crit2 = Critter("Critter 2")
crit3 = Critter("Critter 3")
crit4 = Critter("Critter 4")

Critter.status()

print("\nAccessing the class attribute through an object:", end=" ")
print(crit1.total)

input("\n\nPress the enter key to exit.")