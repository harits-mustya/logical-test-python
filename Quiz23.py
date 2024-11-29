# Quiz 23: Find the Most Frequent Element
# Problem:
# Write a function most_frequent(lst) that returns the most frequently occurring element in the list. If there are multiple elements with the same highest frequency, return any one of them.

# Example:

# python
# most_frequent([1, 3, 1, 3, 2, 1])  # 1
# most_frequent([3, 3, 2, 2, 1])     # 3 or 2

def most_frequent(lst) :
    num = {}
    count = 0

    for i in lst :
        if i in num : num[i] += 1
        else : num[i] = 0
        
    print(num)
    return num
        

most_frequent([1, 3, 1, 3, 2, 1])