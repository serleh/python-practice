#Write a function that takes a list of numbers and returns a list with the squares of those numbers.


# Steps

# 1. define a fumction that accept a list
# 2. create an empty list 
# 3. loop throught the first list and square it, add the values to the new list


def main():
    lst = list(map(int,input("Enter numbers (seperated with comma.) : ").split(",")))
    print(list_squares(lst))


def list_squares(lst):
    squares = [num**2 for num in lst]
    return squares

# def list_squares(lst):
#     squares = []
#     for num in lst:
#         num *=num
#         squares.append(num)
#     return squares
        

if __name__ == "__main__":
    main()
