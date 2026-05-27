# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(51, 100)


# # function definition
# def calc_sum(a, b):  # Parameters
#     return a + b


# sum = calc_sum(1, 2)  # function call; arguments

# # Avg of 3 nos.
# def avg(a, b, c):
#     return (a + b + c)/3

# average = avg(1, 2, 3)
# print(average)

# # Print length of list
# cities = ["Ahmedabad", "Delhi", "Mumbai", "Pune"] #Print list in a single line
# states = ["Gujarat", "Maharashtra", "Rajasthan", "UP", "MP"]
# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end = " ")

# print(len(cities))
# print(len(states))
# print_list(cities)
# # print_list(states)


# # Function to find factorial of n
# def calc_fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)


# calc_fact(30)

# # Function to convert USD to INR
# def converter(usd_val):
#     inr_val = usd_val * 92
#     print(usd_val, "USD = ", inr_val, "INR")
# converter(56)

# Function to check odd even
a = int(input("a = "))

def number(n):
    if a % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

number(a)
