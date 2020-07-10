# Stephen Morris
# Homework 5
# Determines if a user input number of twinkies is less than 100 or greater than 500

# Solicits user input for number of twinkies
twinkiesNum = float(input("How many twinkies do you have? "))
print("You told me you have", twinkiesNum, "twinkies.")
print()

# Checks if twinkies are less than 100, greater than 500, or in between
if twinkiesNum < 100:
    print("Less than 100? Surely you need more twinkies!")
elif twinkiesNum > 500:
    print("More than 500? Where are we going to store all those twinkies?")
else:
    print("We have between 100 and 500 twinkies. Just right!")

# Closing greeting
print()
print("Why are we spending so much time counting twinkies anyways?")
