#Exclusive Network
#Demonstrates logical operator and compound condition

print("\tEclusive Computer Network")
print("\t\tMembers only\n")

security = 0

username = ""
while not username:
    username = input("Username:")

password = ""
while not password:
    password = input("Password:")

if username == "M.Dawson" and password == "Secret":
    print("Hi, Mike.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Hi, Syd")
    security = 3
elif username == "S.Miyamoto" and password == "mario":
    print("Hi Shigeru?")
    security = 3
elif username == "guest" or password == "guest":
    print("welcome guest")
    security = 1
else:
    print("login fails")