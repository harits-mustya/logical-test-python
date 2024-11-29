# Quiz 14: Find the Length of a List
# Write a function find_length(lst) that returns the length (number of elements) of a given list lst.

# Example:
# python
# Copy code
# find_length([1, 2, 3])  # 3
# find_length([10, 20])   # 2

def find_length1(lst) :

    l = list(lst)
    count = 0

    for i in l : count +=1

    print (count)
    return count

find_length1([1,2,3,4,5,6,12,24])

def find_length2(lst) :

    count = len(lst)

    print (count)
    return count

find_length1([1,2,3])