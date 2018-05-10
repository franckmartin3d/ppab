#franck 10/05/2018
#Demonstrate module creation

class Player(object):
    '''A player for a game'''
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question"""
    responce = None
    while responce not in ("y" , "n"):
        responce = input(question).lower
    return responce

def ask_number(question, low, high):
    """Ask for a number within a range."""
    responce = None
    while response not in range(low, high):
        responce = int(input(question))
    return responce

if __name__ == "__main__":
    print("You ran this module directly(and did not import it).")
    input("\n\nPress the enter key to exit.")
