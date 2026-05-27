# for i in range(5):
#     print(i)

# for i in range(0, 101, 2):  # Prints even nos.
#     print(i)

# for i in range(1, 100, 2):  # prints odd nos.
#     print(i)

# for i in range(99, 0, -2):  # Prints odd in reverse
#     print(i)

# for i in range(100, 0, -2):  # prints even in reverse
#     print(i)

# n = int(input("Enter number : "))

# for i in range(1, 11):
#     print(n * i)

# # Sum using Range function
# n = int(input("n : "))
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print("total sum : ", sum)

# Sum using while loop
# n = int(input("n = "))
# i = 0
# sum = 0
# while i <= n:
#     sum = sum + i
#     i+=1
# print(sum)

# Factorial of n using while loop
# n = int(input("n : "))
# fact = 1
# i = 1
# while i<=n:
#     fact = fact * i
#     i+=1
# print(fact)

# Factorial of n using for loop
n = int(input("n = "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)