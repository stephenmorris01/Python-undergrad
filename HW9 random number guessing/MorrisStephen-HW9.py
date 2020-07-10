# Stephen Morris
# Homework 9
# Generates a random number and tracks how many attempts it takes the user to guess it

from random import randint

# Opening greeting
print("I will generate a random number and see if you can guess it.")

# Generates a random number between 1 and 9.
for i in range(1):
    r1 = randint(1, 9)

# Establishes user input, begins tracking number of valid user inputs.
userInput = int(input("Guess an integer from 1 to 9. Or, enter 0 to exit: "))

t1 = 1

if userInput == 0:
    print("Exiting program per user command")
    exit()

while userInput < -1 or userInput > 9:
    print("Value out of range.")
    userInput = int(input("Guess an integer from 1 to 9. Or, enter 0 to exit: "))

while 1 <= userInput <= 9:

    if userInput == 0:
        print("Exiting program per user command")
        exit()

    elif userInput < r1:
        print("Too small, try again!")
        t1 = t1 + 1
        userInput = int(input("Guess an integer from 1 to 9. Or, enter 0 to exit: "))

    elif userInput > r1:
        print("Too large, try again!")
        t1 = t1 + 1
        userInput = int(input("Guess an integer from 1 to 9. Or, enter 0 to exit: "))

    elif userInput == r1:
        print("Exactly right!")
        print("That took you", t1, "tries.")
        exit()
