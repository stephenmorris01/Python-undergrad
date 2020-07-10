# Stephen Morris
# Homework 3
# Calculates the square, cube, and fourth power of a user input integer

# Solicits user input
userNumber = int(input("I will calculate exponents up to the fourth power. Give me a whole number to calculate: "))
print()

#Calculates the square
print("%-24s" % "the square is: ", "%10d" % userNumber ** 2)

#Calculates the cube
print("%-24s" % "the cube is: ", "%10d" % userNumber ** 3)

#Calculates the fourth power
print("%-24s" % "the fourth power is: ", "%10d" % userNumber ** 4)

#Calculates the fifth power
print("%-24s" % "the fifth power is: ", "%10d" % userNumber ** 5)
print()

#Closing greeting
print("Have a great day!")