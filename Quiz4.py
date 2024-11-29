# 4. Count Vowels in a String
# Write a function count_vowels(s) that counts the number of vowels (a, e, i, o, u) in a given string s.

# Example:

# python
# count_vowels("hello world")  # 3

def count_vowels(s) :
    
    vowels = "aeiueoAIUEO"
    count = 0

    for char in s :
        if char in vowels : count+=1
    
    print (count)
    return count

count_vowels("xyr")