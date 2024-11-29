# Quiz 12: Reverse a String
# Write a function reverse_string(s) that returns the reverse of the given string s.

# Example:
# python
# reverse_string("hello")  # "olleh"
# reverse_string("Python")  # "nohtyP"

def reverse_string(s) :

    reverse_list = s[::-1]

    print(reverse_list)
    return reverse_list

reverse_string("Hello")