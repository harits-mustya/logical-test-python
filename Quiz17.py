# Quiz 17: Fibonacci Sequence
# Write a function fibonacci(n) that returns the nth number in the Fibonacci sequence.

# Example:
# python
# fibonacci(5)  # 5
# fibonacci(8)  # 21

def fibonacci(n) :
    
    if n <= 0 : return 1
    fib = 0
    fib1 = 0
    fib2 = 1
    fib3 = 0

    for i in range(n) : 
        fib3 = fib1 + fib2
        fib1 = fib2 
        fib2 = fib3
    
    print(fib1)
    return fib1

fibonacci(8)

def fibonacci2(n):
    if n <= 0:
        return 0  # Fibonacci of 0 is typically 0
    elif n == 1:
        return 1  # Fibonacci of 1 is 1
    
    fib1 = 0
    fib2 = 1
    
    for _ in range(2, n + 1):  # Start from 2 because we already have first two values
        fib_next = fib1 + fib2
        fib1 = fib2
        fib2 = fib_next
    
    return fib2  # fib2 now holds the nth Fibonacci number

# Test cases
print(fibonacci2(5))  # 5
print(fibonacci2(8))  # 21
