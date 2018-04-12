#franck 12/04/2018
#High score 2.0
#demonstrate nested sequence

scores = []

choice = None
while choice != "0":
    print("""
    High score 2.0
    0 - Quit
    1 - List Score
    2 - Add a score
    """)

    choice = input("Choices: ")
    print()

    #exit
    if choice == "0":
        print("Good-bye.")

    #Display hight-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name,"\t", score)

    # add a score
    elif choice =="2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?"))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        #keep only 5 high score
        scores = scores[:5]

    #Some unknow choice

    else:
        print("Sorry, but ", choice, "isnt a valid choice.")

input("\n\nPress the enter key to exit.")




