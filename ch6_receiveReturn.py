#Franck 20/04/18
# receive and return
# Demonstrate parameters and returns values



def display(message):
    print(message)

def give_me_five():
    five = 5
    return 5

def ask_yes_no(question):
    '''Ask a yes or no question'''

    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

#main
display("Here'a message for you.\n")

number = give_me_five()
print("Here's what i got from give_me_five():", number)

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

input("\n\npress the enter key to exit")
