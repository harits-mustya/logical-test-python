# Quiz 11: Find Largest Element in a List
# Write a function find_largest(lst) that returns the largest element in a given list of numbers.

# Example:
# python
# find_largest([1, 2, 3, 4, 5])  # 5
# find_largest([10, 20, 5, 30])  # 30

def find_largest(lst) :
    max = lst[0]

    for num in lst : 
        if num > max : max = num
    
    print(max)
    return max

find_largest([1, 2, 3, 4, 5])
find_largest([10, 20, 5, 30])

def find_smallest(lst) :
    min = lst[0]

    for num in lst : 
        if num < min : min = num
    
    print(min)
    return min

find_smallest([1, 2, 3, 4, 5])
find_smallest([10, 20, 5, 30])