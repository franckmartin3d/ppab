#franck 11/04/2018
# Demonstrate list methods


#empty list
score = []

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

#commit