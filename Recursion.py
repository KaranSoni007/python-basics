# # Recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)


# # Factorial using Recursion
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

# print(fact(5))

# # Sum using Recursion
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1) + n
# a = sum(10)
# print(a) 

# Print all elements from list using recursion
i = 0
def print_list(list, i):
    if(i == len(list)):
        return
    print(list[i])
    print_list(list, i+1)

fruits = ["mango", "apple", "banana"]
a = print_list(fruits, i)
print(a)