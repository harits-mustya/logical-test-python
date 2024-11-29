# 7. Prime Number Check
# Write a function is_prime(n) that checks whether a given number n is a prime number.

# Example:

# python
# is_prime(7)   # True
# is_prime(10)  # False

def is_prime(n) :

    if n <= 1 : return false

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("False")
            return False
    
    print ("True")
    return True

is_prime(7)