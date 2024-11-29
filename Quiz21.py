# Quiz 21: Find Second Largest Number
# Problem:
# Write a function find_second_largest(lst) that returns the second largest number in a given list. If the list has fewer than 2 distinct numbers, return None.

# Example:

# python
# find_second_largest([10, 20, 4, 45, 99])  # 45
# find_second_largest([4, 4, 4])            # None
# find_second_largest([1])                  # None

def find_second_largest(lst) :
    unique_set = set(lst)
    unique_list = sorted(list(unique_set),reverse=True)
    count = len(unique_set)

    if count < 2 : return None
    else : print(unique_list[1])

find_second_largest([10, 20, 4, 45,112, 99])
find_second_largest([10, 10, 20])
find_second_largest([4, 4, 4])
find_second_largest([1]) 