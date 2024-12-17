# x = int(input("What's X? "))
# y = int(input("What's y? "))


# if x !=y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# 1. Even or Odd
# Write a program that:

# Takes a number as input from the user.
# Prints whether the number is even or odd.



def is_even():
    number = int(input("X: "))
    return  number % 2 ==0

print(is_even())