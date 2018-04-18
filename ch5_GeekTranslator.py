#franck 17/04/2018

# greek translator
# Demonstrate using dictionaries

geek = {"404": "Clueless. from the web error message 404, meaning page not found",
        "Googling": "seraching the internet for background information on a person",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to makeit work.",
        "Uninstalled": "being fired. Especially popular during the dot-bomb era.",
        }

choice = None
while choice != "0":

    print("""
    Geek Translator
     0 - Quit
    1 - Look Up a Geek Term
    2 - Add a Geek Term
    3 - Redefine a Geek Term
    4 - Delete a Geek Term

    """
    )

    choice = input("Choice: ")
    #just a white line
    print()

    #exit
    if choice == "0":
        print("Goodbye!")

    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek:
            deinition = geek[term]
            print("\n" , term, "means", deinition)
        else:
            print("\n Sorry, I dont know" , term)

    # add a term-definition pair
    elif choice == "2":

        #define the key
        term = input("What term do you want me to add?: ")

        if term not in geek:
            definition = input("what is the definition?: ")

            #add key and definition to geek directory
            geek[term] = definition
            print("\n", term , "has been added.")
        else:
            print("\n That term already exist!")

    # replace a key
    elif choice == "3":
        term = input("What term do you want to refine?: ")
        if term in geek:
            definition = input("Whats the definition?:")
            geek[term] = definition
            print("\n", term, "has been refined.")
        else:
            print("\n that term doesnt exist! try adding it.")

    #delete a term-definition pair
    elif choice == "4":
        term = input("what term you want to delete?: ")
        if term in geek:
            del geek[term]
            print("\nOkay, i deleted", term)

        else:
            print("\n I cant do that", term, "doent exist in the dictionary.")

# some unknown choice
    else:
    print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")



