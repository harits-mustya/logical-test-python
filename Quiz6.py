# 6. Factorial Calculation
# Write a function factorial(n) that calculates the factorial of a number n.

# Example:

# python
# factorial(5)  # 120 (5 * 4 * 3 * 2 * 1)

def factorial(n) :
    factorial = 1

    for i in range(2,n+1): factorial *= i

    print(factorial)
    return factorial

factorial(10)
