# Quiz 13: Check if a Number is Even or Odd
# Write a function is_even_or_odd(n) that checks whether the given number n is even or odd.

# Example:
# python
# Copy code
# is_even_or_odd(4)  # "Even"
# is_even_or_odd(7)  # "Odd"

def is_even_or_odd1(n) :

    if n <=0 : return False

    if n % 2 == 0 : print("Even")
    else : print("Odd")

    return n

is_even_or_odd1(654)

# def is_even_or_odd2(n) :

#     if n <=0 : return False

#     if n in range(2,n+1,2) : print("Even")
#     else : print("Odd")

#     return n

# is_even_or_odd2(1)