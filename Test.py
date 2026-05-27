# # Create set with 5 items
# set1 = {1, 2, 3, 4, 5}
# print(set1)

# # Add
# set1.add(6)
# set1.add(7)
# print(set1)

# # Remove
# set1.remove(6)
# print(set1)

# s= frozenset(set1)
# print(s)

str = "python program"
print(str.split())
print(str.upper())
print(str.lower())
print((str[:7]).upper()+str[7:])

print(str.replace("python", "react"))

str2="mississipi"
# Count of i
print(str2.count("i"))

# MISsissipi
print((str2[:3]).upper()+str2[3:].lower())

# Replace i with t
print(str2.replace("i", "t"))

# Reverse using slicing
print(str2[::-1])

# Index of i
print(str2.index("i"))