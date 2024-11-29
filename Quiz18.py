# Quiz 18: Merge Two Sorted Lists
# Write a function merge_sorted_lists(list1, list2) that merges two sorted lists into a single sorted list.

# Example:
# python
# Copy code
# merge_sorted_lists([1, 3, 5], [2, 4, 6])  # [1, 2, 3, 4, 5, 6]
# merge_sorted_lists([1, 2, 8], [3, 4, 5])  # [1, 2, 3, 4, 5, 8]

def merge_sorted_lists(list1,list2) :

    merge = sorted(list1 + list2)
    
    print (merge)
    return merge

merge_sorted_lists([1, 3, 5], [2, 4, 6])

def merge_sorted_lists2(list1, list2):
    merged = []
    i, j = 0, 0
    
    # Use two pointers to merge the lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from list1 or list2
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    print(merged)
    return merged

merge_sorted_lists2([1, 3, 5], [2, 4, 6])


