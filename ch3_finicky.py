# Franck 31/03/2018
#Finicky
#Demonstrates the break and continue statement

count = 0
while True:
    count += 1
    #end loop if count greater than 10
    if count > 10:
        break
    # skip 5
    if count == 5:
        continue
    print(count)
print("\n\nPress the enter key to exit.")

