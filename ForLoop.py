# # Q.1
# num = [1, 2, 3, 4, 5]

# for x in num:
#     print(x)

# # Q.2
# tup = "Karan"

# for x in tup:
#     if x == "a":
#         print("a found")
#         continue
#     print(x)

# # Q.3 print list
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for x in num:
#     print(x)

# Q.4 search number
num = [100, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
a = 100
for x in num:
    if(x == a):
        print("x found at index ", i)
    i+=1