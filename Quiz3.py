# 3. Sum of Even Numbers
# Write a function sum_of_evens(n) that returns the sum of all even numbers from 1 to n.

# Example:

# python
# sum_of_evens(10)  # 30 (2 + 4 + 6 + 8 + 10)

def sum_of_evens(number):
    
    if number <= 0 : return 0
    
    sum = 0
    for n in range(2,number+1,2) : sum += n

    print(sum)
    return sum

sum_of_evens(50)