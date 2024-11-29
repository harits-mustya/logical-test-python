# 5. Find the Largest Number in a List
# Write a function find_max(lst) that takes a list of numbers and returns the largest number.

# Example:

# python
# find_max([1, 3, 7, 2, 5])  # 7

def find_max(lst) :

    max = lst[0]
    count = 0
    
    for num in lst :
        if num > max : max = num
    
    print (max)
    return max

find_max([1,2,4,3,7])
     