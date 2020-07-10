# Stephen Morris
# Homework 8
# Counts by twos to reach the user's age

# Opening greeting
print("I will count by twos until I reach your age.")

# Solicits user input for age
userAge = int(input("How old are you?: "))
print("You are", userAge, "years old")

# Adds two to the user's input in order to stop with the user's age, not before.
userAge = userAge + 2

# Checks if user's age is even or odd, then counts by twos
if userAge % 2 == 0:
    print("Your age is an even number, so I'll start at 2.")
    for x in range(2, userAge, 2):
        print(x)
else:
    print("Your age is an odd number, so I'll start at 1.")
    for x in range(1, userAge, 2):
        print(x)

# Closing greeting
print()
print("Try again next year for a different result!")
