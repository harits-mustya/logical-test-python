# Quiz 9: Count Words in a String
# Write a function count_words(s) that counts the number of words in a given string s. A word is defined as any sequence of characters separated by spaces.

# Example:
# python
# count_words("Hello, how are you?")  # 4
# count_words("This is a test.")      # 5

def count_words(s) : 
    
    words = s.split()
    count = len(words)

    print (count)
    return count

count_words("Hello, how are you?")
count_words("This is a test .") 