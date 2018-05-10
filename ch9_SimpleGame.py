#frank 10/05/2018
#Simple Game

import ch9_GamesModule, random

print("Welcome to the world's simplest game!\n")

again = None
while again != "n":
    players = []
num = ch9_GamesModule.ask_number(question= "how many players? (2-5)", low = 2, high = 5)

for i in range(num):
    name = input("player name:")
    score = random.randrange(100) + 1
    player = ch9_GamesModule.Player(name, score)
    player.appen(players)

print("\nHere are the game results:")
for player in players:
    print(player)

again = ch9_GamesModule.ask_yes_no("\nDo you want to play again? (y/n): ")

input("\n\nPress the enter key to exit.")


