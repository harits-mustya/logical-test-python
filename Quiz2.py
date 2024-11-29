# 2. Palindrome Check
# Write a function is_palindrome(s) 
# that checks whether a given string s is a palindrome (reads the same forward and backward). 
# Ignore spaces and case sensitivity.

# Example:
# is_palindrome("Racecar")  # True
# is_palindrome("hello")    # False

def is_palindrome (s) : 

    normalized_s = ''.join(s.lower().split())

    char_list = list(normalized_s)
    reverse_char_list = char_list[::-1]

    if char_list == reverse_char_list : print("True")
    else : print ("False")

    return char_list == reverse_char_list

is_palindrome("Racecar")
is_palindrome("Hello 2")