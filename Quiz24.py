

def sum_of_squares(n):

    n = abs(n)
    total = 0

    for i in range(1,n+1) :
        total += i * i
    print(total)

sum_of_squares(3)
