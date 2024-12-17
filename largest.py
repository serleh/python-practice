# Largest of Three Numbers
# Create a program that:

# Accepts three numbers from the user.
# Prints the largest number.


def largest():
    x = int(input('X: '))
    y = int(input('Y: '))
    z = int(input('Z:'))

    return max(x,y,z)

print(largest())