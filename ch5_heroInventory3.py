#franck
#04/04/2018
#finish on 10/04/2018
# Hero's Inventory 3.0
# Demonstrate lists

# create a list with some items and display with a for loop
inventory = ["sword", "armor", "shield", "axe", "healing potion"]
print("your items:")
for item in inventory:
    print(item)

input("n\Press the enter key to continue.")

# get the length of a list
print("You have",len(inventory), "items in your posessions.")

input("n\Press the enter key to continue.")

# test for membership operator with in
if "healing possion" in inventory:
    print("You will live to fight another day")

#Display one item trought an index
index = int(input("\nEnter the index number for an item in inventory:"))
print("at index", index, "is", inventory[index])

#display a slice
start = int(input("\nEnter the index number to start slice:"))
finish = int(input("\nEnter the index number to finish slice:"))

print("inventory[" ,start, ":", finish, "] is ", end="")
print(inventory[start:finish])

input("n\Press the enter key to continue.")

#Concatenate two list (add them together)
chest = ["gold", "booty"]
print("You find a chest witch contains:")
print(chest)
print("you add the contents of the chest to your inventory")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("n\Press the enter key to continue.")

#Assign by index
print("you trade your sword for a crossbow")
inventory[0] = "crossbow"
print("Your inventory is now")
print(inventory)

input("n\Press the enter key to continue.")

#assign by slice
print("You use your gold and gems to buy an orb of future telling")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now")
print(inventory)

input("n\Press the enter key to continue.")

#Delete an element















