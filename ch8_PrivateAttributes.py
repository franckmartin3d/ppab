#francois Martin 01/05/2018
#Private Critter
#Demonstrates private variable and methods

class Critter(object):
    '''A virtual pet'''
    def __init__(self, name , mood):
        print("A new critter has been born!")
        self.name = name        #public
        self.__mood = mood      #Private

    def talk(self):
        print("\nI'm", self.name)
        print("right now i feel", self.__mood, "\n")

    def __private_method(self):
        print("this is a private method")

    def public_method(self):
        print("this is a public method")
        self.__private_method()

#main
crit = Critter(name = "poochie", mood = "murder")
crit.talk()
crit.public_method()

input("\n\nPress the enter key to exit")
