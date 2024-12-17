# Merge Two Sorted Lists: Write a function that merges two sorted lists into one sorted list.


lst1 = [1,23,4,5,6]
lst2 = [3,4,5,6,7,]

lst1.sort()
lst2.sort()

lst1= lst1.append(lst2)
lst1.sort()
print(lst1)