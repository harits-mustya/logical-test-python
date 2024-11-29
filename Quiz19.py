# Quiz 19: Count Words Starting with a Specific Letter
# Write a function count_words_starting_with(lst, letter) that counts how many words in a given list start with a specific letter (case-insensitive).

# Example:
# python
# count_words_starting_with(["apple", "banana", "avocado", "grape"], "a")  # 2
# count_words_starting_with(["dog", "cat", "elephant", "deer"], "d")      # 2

def count_words_starting_with(lst, letter):

    count = 0

    for words in lst :
        if words.lower().startswith(letter.lower()) : count += 1
    
    print(count)
    return count

count_words_starting_with(["apple","banana","avocado"], "a")
