#franck 3/13/18
#ch3 Losing Battle
#demonstrate the infinite loop

print("Your hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies strect out. melting in the horizon.")
print("Your hero unsheathes is sword for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while health != 0:
    trolls += 1
    health -= damage

    print("Your hero swings and defeats an evil troll, but takes ", damage, "damage points")

print("your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero was defeatead")

in

