#franck
#04/04/2018

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
print("You find a chest wich contains:")
print(chest)
print("you add the contents of the chest to your inventory")
