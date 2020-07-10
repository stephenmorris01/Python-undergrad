# Stephen Morris
# Final Exam
# Computes the user's (saleswoman's) commission based on sales and commission rate

# Opening greeting
print("Hello, I will compute your commission earned during this month.")
print()

# Solicits user input for sales
salesAmount = float(input("What were your total sales? Enter a whole dollar or decimal amount: "))
print("You totaled $", "%.2f" % salesAmount, "dollars")
print()

# Solicits user input for commission rate
commissionRate = float(input("What is your commission rate? Enter a whole number or decimal and I'll convert it to a "
                             "percent: "))
print("Your rate is", commissionRate, "%")
print()

# Computes the commission earned in dollars
commissionEarned = salesAmount * (commissionRate / 100)
print("Congratulations! You earned $", "%.2f" % commissionEarned, "in commission!")
print()

# Closing greeting

print("Remember your ABC's... Always Be Closing!")
