#franck 11/04/2018
# Demonstrate list methods


#empty list
scores = []

#initialize variable (make it something)
choice = None

#continues until the user enters 0.
while choice !="0":
    print(
    """
    High Scores
    
    0 - EXIT
    1 - Show Scores
    2 - Add a score
    3 - Delete a score
    4 - Sort Score
    """
    )

    choice = input("Choice: ")
    print()
#exit
    if choice == "0":
        print("Goodbye!")
     # list high-score
    elif choice =="1":
        print("Hight Score")
        for score in scores:
            print(score)

    #add a score
    elif choice =="2":
        score = int(input("whats score did you get?:"))
        scores.append(score)

    #remove a score
    elif choice == "3":
        score = int(input("Romove which score?:"))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isnt in the high score list.")

    #Sort score
    elif choice == "4":
        scores.sort(reverse=True)

    # Some unknow choice
    else:
        print("Sorry, but ", choice, "isn't a valid choice")

input("\n\nPress the enter key to exit.")
