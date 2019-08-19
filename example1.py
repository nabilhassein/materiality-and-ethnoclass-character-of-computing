### PART 1: interactive user input, conditionals
username = input("what is your name? ")  # the variable "username" will store what the user types in

if username == "nabil":  # this is a test for equality, with two ==
    print("we have the same name, " + username)
else:
    print("we have different names, " + username)

## exercises:
# Modify the above code to work with your own name.
# Get more user input into more variables. Use that data inside your conditional.
# challenge: set up a password to go with the username. Display certain information only to people who know it.
# challenge: google "python3 unicode" and learn to use non-English characters in your strings.
