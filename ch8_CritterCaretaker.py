#francois Martin 01/05/2018
#Citter Caretaker
#A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name , hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhapyness = self.hunger + self.boredom
        if unhapyness < 5:
            m = "Happy"
        elif 5 <= unhapyness <= 10:
            m = "okay"
        elif 11 <= unhapyness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and i feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brrupp. thank you")
        self.hunger -= food
        if self.hunger < 0 :
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Whats do you want to call yoiur critter?:")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
            Critter Caretaker
            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)
        choice = input("Choice: ")

        #exit
        if choice == "0":
            print("good Bye.")

        # Listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
print("\n\nPress the enter key to exit.")



