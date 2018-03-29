#franck 10/03/18
#trust fund buddy - bad
#demonstrate logical errors

print(
    '''
        Trust fund buddy
        
Total your montly spending so that your trust fund doesnt run out
(and youre forced to get a real job).

please enter the requested, monthly cost. since youre rich ignore
pennies and use only dollars
        '''
)
car = int(input("lambourgini tune ups:"))
rent = int(input("manatahn appartmen:"))
jet =int(input("private jet:"))
gift = int(input("Gifts:"))
food = int(input("food:"))
staff = int(input("Staff (buttler chef etc"))
guru = int(input("coach:"))
games = int(input("computer games:"))

total = car + rent + jet + gift + food + staff + guru + games

print("\nGrand total:",total)
input("\n\nPress enter to exit.")