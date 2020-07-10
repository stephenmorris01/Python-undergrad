# Stephen Morris
# Homework 7
# Provides analysis of whether the user should eat a certain number of cookies

# Solicits user input for number of cookies
cookies = float(input("How many cookies do you have?: "))
print("You told me you have", cookies, "cookies")
print()

# Checks if the cookies are less than 10, less than 30, less than 50, or if there are 50 or more cookies
if cookies < 10:
    print("only", cookies, "cookies?")
    print("I can eat those cookies!")
elif cookies < 30:
    print("Wow,", cookies, "cookies?")
    print("It'll be a struggle, but I can take 'em!")
elif cookies < 50:
    print("You can't be serious.", cookies, "cookies?")
    print("That's too many!")
else:
    print("If you are considering eating 50 or more cookies, "
          "you are going to need a doctor or a better life insurance policy!")

# Closing greeting
print()
print("Enjoy those cookies!")
