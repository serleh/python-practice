# Odd and Even Split: Write a function that separates the odd and even numbers from a list into two different lists.

def main():
    lst = list(map(int,input("LIST: ").split(",")))
    odd_lst,even_lst = odd_even_split(lst)
    print(f"ODD LIST: {odd_lst}")
    print(f"EVEN LIST: {even_lst}")





def odd_even_split(lst):
    odd_lst = [num for num in lst if num%2 !=0]
    even_lst = [num for num in lst if num%2 ==0]
    return odd_lst , even_lst


if __name__ == "__main__":
    main()
