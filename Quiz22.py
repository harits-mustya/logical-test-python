# Quiz 22: Generate a Multiplication Table
# Problem:
# Write a function multiplication_table(n) that prints the multiplication table for numbers from 1 to n.

# Example:

# python
# multiplication_table(3)
# # Output:
# # 1 x 1 = 1
# # 1 x 2 = 2
# # 1 x 3 = 3
# # 2 x 1 = 2
# # 2 x 2 = 4
# # 2 x 3 = 6
# # 3 x 1 = 3
# # 3 x 2 = 6
# # 3 x 3 = 9

def multiplication_table(n) :
    n = abs(n)
    if n <= 0 : return 1

    for i in range(1,n+1) :
        for j in range(1,n+1):
            # result = str(i) + " x " + str(j) + " = " + str(i*j)
            # print(result)
            print(f"{i} x {j} = {i * j}")
        print()
    
multiplication_table(3)

# def multiplication_table2(n):
#     if n <= 0:
#         print("Please provide a positive integer.")
#         return None

#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(f"{i} x {j} = {i * j}")
#         print()  # Blank line between tables for readability

# # Test with 3 and 5
# multiplication_table2(1)
