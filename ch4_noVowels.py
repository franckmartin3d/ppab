#franck
#02/042018

# No vowels
# Demonstrate creating new strings with a for loop

message = input("enter a new message: ")
new_message = ""
vowels = "aeiou"

print( )
for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
        print ("A new string as been created:", new_message)
print("\nYour message witot vowel is:", new_message)
input("\nPress enter to exit")
