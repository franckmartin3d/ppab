#franck
#02/042018

#Message Analyzer
#Demonstrates the len() function and the in operator

message = input("Enter a message:")
print("\nThe lenght of your message is: ", len(message))

print("\nThe most common letter in the english language is 'e',")
if "e" in message:
    print("it is in your message")
else:
    print("it is not in your message.")

input("\n\nPress enter to exit.")