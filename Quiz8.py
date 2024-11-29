# 8. Find Common Elements
# Write a function find_common_elements(list1, list2) that returns a list of elements that are present in both list1 and list2.

# Example:

# python
# find_common_elements([1, 2, 3], [2, 3, 4])  # [2, 3]

def find_common_elements(lst1,lst2) :

    same = [item for item in lst1 if item in lst2]
    print(same)
    return same

find_common_elements([1,2,3], [2,4,3])