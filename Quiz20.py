# Quiz 20: Sum of Digits
# Write a function sum_of_digits(n) that returns the sum of digits in the given number n.

# Example:
# python
# Copy code
# sum_of_digits(123)  # 6
# sum_of_digits(9876) # 30

def sum_of_digits (n) :
    n = abs(n)

    number = str(n)

    sum = 0
    for i in number : sum += int(i)

    print(sum)

sum_of_digits (-9876)
