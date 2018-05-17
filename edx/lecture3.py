#edX week 2

# -----------Guess andCheck cube root--------------

# cube = 8
# for guess in range (cube + 1):
#     if guess**3 == cube:
#         print("Cube root of", cube, "is", guess)


# -----------Guess andCheck cube root--------------

cube = 8

# Abs is absolute value ,0 to 8
# for guess in range (abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
#
#
# if guess**3 != abs(cube):
#     print(cube, "is not a perfect cube")
# else:
#     if cube < 0:
#         guess = -guess
#     print("cube root of " + str(cube) + " is " + str(guess))


# -----------Approximate solution Cube Root--------------

# #initializing variable
# cube = 27
# epsilon = 0.01
# guess = 0.0
# increment = 0.0001
# num_guesses = 0
#
# # loop guees x guees x guess - cube if that is not good enought keep guessing
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
#
# print("num_guesses = ",num_guesses )
#
# if abs(guess**3 - cube) >= epsilon:
#     print("failed on cube root of", cube)
# else:
#     print(guess, "is close to the cube root of", cube)


# -----------Bisection Search--------------

cube = 27
epsilon = 0.01
num_guess = 0
low = 0  #bundaries
high = cube #bundaries

guess = (high + low)/2.0 # guess halfway in between

while abs(guess**3 - cube) >= epsilon:
    # My guess is too low set the low bundari to be the guess
    if guess**3 < cube:
        low = guess
    # My guess is too high set the high bondari to be the guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guess += 1

print("num_guesses = ", num_guess)
print(guess, " is close to the cube root of ", cube)







