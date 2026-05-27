# # Q.1 Print 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1

# Q.2 Print 100 to 1
# i = 100
# while i >=1:
#     print(i)
#     i -= 1

# Q.3 Table of 3
# n = int(input("Enter n : "))
# i = 1
# while i<=10:
#     print(n * i)
#     i += 1

# Q.4 print list

# list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

# Q.5 search for a number x in given tuple

tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49
i = 0
while i < len(tup1):
    if tup1[i] == x:
        print(x, "is found at index", i)
    i += 1


# Continue statements
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1


# Break statements
i = 1
while i<=10:
    if i == 3:
        break
    print(i)
    i+=1