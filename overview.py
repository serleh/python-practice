# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# age = int(input("Enter your age: "))
# print(f"Next year, you will be, {age + 1}!")

# x = 42
# print(type(x))

x = 10 # Global scope

# def func():
#     y = 5 # local scope
#     print(y)

# func()
# print(x)

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Saleh"))

# pi = 3.14159
# print(f"{pi:.2f}")

# large_numbers = 10000000
# print(f"{large_numbers:,}")






# Create a program that:

# Takes the user's name and age as input.
# Prints a formatted greeting.
# Calculates and displays their age in 5 years.
# Formats a large number (e.g., population of a city) with commas.

# def main():
#     greetings()


# def greetings():
#     name = input("Enter your name: ")
#     age = int(input("Enter you age: "))

#     print(f"Good Morning {name}! How's python going?")
#     print(f"{name} in 5 years you will be {age + 5} years old.")


# main()

# kano_state_population = 10000000000

# print(f"Kano state population is: {kano_state_population:,}")



# Input and String Manipulation
# Write a program that:
# Takes a sentence as input.
# Converts it to uppercase and prints it.
# Splits the sentence into words and prints the list of words.

# sentence = input("Enter a sentence: ").upper()
# print(sentence)

# sentence =sentence.split()
# print(sentence)


# def create_sentence():
#     sentence = input("Enter a sentence: ").upper()
#     sentence =sentence.split()
#     print(sentence)

#     return sentence


# create_sentence()




# Data Types
# Create a program that:

# Prompts the user to enter their height in centimeters.
# Converts the input to a float.
# Calculates and displays the height in meters.
# Take two numbers as input from the user:

# Add, subtract, multiply, and divide them.
# Display the results with appropriate data types.



# heght = int(input("Enter height in (cm): "))
# print(f"Your height is { heght:.2f} cm")

# def main():
#      x = int(input("Enter num1: "))
#      y = int(input("Enter num2: "))

#      return calculator(x,y)





# def calculator(num1,num2):
   
#     sum = num1 + num2
#     difference = num1 - num2
#     product = num1 * num2
#     div = num1 / num2

#     print(f"{num1} + {num2} = {sum}")
#     print(f"{num1} - {num2} = {difference}")
#     print(f"{num1} * {num2} = {product}")
#     print(f"{num1} / {num2} = {div}")

# main()




# Create a function convert_temperature() that:

# Takes a temperature in Celsius as input.
# Converts it to Fahrenheit using the formula 
# 𝐹
# =
# 𝐶
# ×
# 9
# 5
# +
# 32
# F=C× 
# 5
# 9
# ​
#  +32.
# Returns the converted value.



def convert_temperature(c):
    f = c *(9/5 ) + 32
    return f


print(convert_temperature(22))




































