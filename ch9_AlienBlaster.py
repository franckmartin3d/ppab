#Franck 04/05/2018
#Alien Blaster
#Demonstrate object interaction

class Player(object):
    """A Player in a shooting game."""
    def blast(self, enemy):
        print("The player blast an enemy.\n")
        enemy.die()

class Alien(object):
    """An alien in a shooter game."""
    def die(self):
        print("The alien gasp he dies!")

# main
print ("\t\tDeath of an Alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress The enter key to exit.")