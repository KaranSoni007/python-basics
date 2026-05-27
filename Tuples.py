# Tuples in Python

# a built-in data type that lets us create immutable sequence of values

tup = (1, 2, 3, 4, 5)
# tup2 = (1,)
print(tup)
print(type(tup))

# Check for palindrome
list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

# Sorting the tuple
tuple1 = ("C", "D", "A", "A", "B", "B", "A")
print(tuple1)

# Sorting the list
new_list = ["C", "D", "A", "A", "B", "B", "A"]
new_list.sort()
print(new_list)

