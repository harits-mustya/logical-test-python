# Quiz 15: Count Occurrences of an Element
# Write a function count_occurrences(lst, element) that counts how many times the element appears in the list lst.

# Example:
# python
# Copy code
# count_occurrences([1, 2, 3, 2, 4], 2)  # 2
# count_occurrences([1, 1, 1, 1], 1)    # 4

def count_occurrences(lst,element) :

    count = 0
    for elm in lst :
        if elm == element : count += 1
    
    print(count)
    return count

count_occurrences([1, 1, 3, 2, 4], 3)
count_occurrences([1, 1, 1, 1], 1) 