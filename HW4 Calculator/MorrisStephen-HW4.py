# Stephen Morris
# Homework 4
# Calculates sum, difference, product, average, maximum, and minimum of 2 user input numbers

# Solicits user input 1
userNumber1 = float(input("Please give me your first number to calculate: "))
print("The first number is", userNumber1)
print()

# Solicits user input 2
userNumber2 = float(input("Please give me your second number to calculate: "))
print("The second number is", userNumber2)
print()

# Calculates the sum
print("%-24s" % "the sum is: ", float(userNumber1 + userNumber2))

# Calculates the difference
print("%-24s" % "the difference is: ", float(userNumber1 - userNumber2))

# Calculates the product
print("%-24s" % "the product is: ", float(userNumber1 * userNumber2))

# Calculates the average
print("%-24s" % "the average is: ", float((userNumber1 + userNumber2) / 2))

# Calculates the maximum
print("%-24s" % "the larger value is: ", float(max(userNumber1, userNumber2)))

# Calculates the minimum
print("%-24s" % "the larger value is: ", float(min(userNumber1, userNumber2)))

print()

# Closing greeting
print("I hope you enjoyed saving some time. Have a coffee to celebrate!")
