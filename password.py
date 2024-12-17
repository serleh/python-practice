# Password Strength Checker
# Write a program that:

# Takes a password as input.
# Checks its strength:
# If the length is less than 6, print "Weak".
# If the length is between 6 and 12, print "Moderate".
# If the length is greater than 12, print "Strong".


def password_strength():
    password = input("Password: ")

    if len(password) < 6:
        print("Weak")
    elif len(password)  <=12:
        print("Moderate")
    elif len(password) > 12:
        print("Strong")


password_strength()