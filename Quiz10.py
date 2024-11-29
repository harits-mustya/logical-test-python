# Quiz 10: Sum of Digits
# Write a function sum_of_digits(n) that returns the sum of all the digits in a given number n.

# Example:
# python
# sum_of_digits(123)  # 6 (1 + 2 + 3)
# sum_of_digits(987)  # 24 (9 + 8 + 7)

def sum_of_digits(n) :

    total = 0

    for digit in str(n) : total += int(digit)

    print(total)
    return total

sum_of_digits(987)