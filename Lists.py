# Lists in Python

# A built-in datatype that stores set of values
# It can store elements of different types like int, float, string etc.
# Lists are mutable

marks = [67, 56, 79, 77, 89]

student = ["Karan", 85, "Ahmedabad"]
student[0] = "Jay"
print(len(student))
print(student)

# List Slicing
print(marks[1:4])
print(marks[-4:-2])

# List Methods
# Append
marks.append(99)
print(marks)

# Sort
marks.sort()
print(marks)

# Reverse
marks.reverse()
print(marks)

# Insert
marks.insert(0, 50)
print(marks)

# Pop
marks.pop(0)
print(marks)

# Remove
marks.remove(79)
print(marks)