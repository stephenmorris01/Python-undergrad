# Stephen Morris
# Homework 6
# Determines if a user input monetary value is between 100 and 500, or between 1000 and 5000

# Solicits user input for monetary value
money = float(input("Input the dollar amount: "))
print("You told me you have", money, "dollars")
print()

# Checks if value is between 100 and 500, or between 1000 and 5000
if 100 <= money <= 500:
    print(money, "is between 100 and 500")
    print("This meets the stated criteria")
elif 1000 <= money <= 5000:
    print(money, "is between 1000 and 5000")
    print("This meets the stated criteria")
else:
    print(money, "is not between 100 and 500 or between 1000 and 5000")

# Closing greeting
print()
print("Have a great day!")
