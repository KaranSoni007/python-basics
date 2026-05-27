# User Input
Name = input("Name : ")
Age = int(input("Age : "))
print("My name is", Name, "and I am", Age, "years old")

# String methods
# Concatenation of 2 strings
a = "Hello"
b = "Python"

print(a + b)
print(a + " " + b)
print(a + "\n" + b)
print(a + "\t" + b)
print(len(a))

# Indexing/Positioning of letters in string
# We can print or access the string characters on a particular index.
# But, we can't modify it.
print(a[0])
print(b[0])

# String methods
str = "volkswagen is a german company"

# Uppercase
print(str.upper())

# Lowercase
print(str.lower())

# Slicing
print(str[1:5])

# Reverse/Negative Slicing
print(str[-8:-2])

# Check if string ends with()
print(str.endswith("er"))

# Replace
print(str.replace("volkswagen", "skoda"))

# Capitalize
print(str.capitalize())

# Check a num is odd or even
num = int(input("Enter a number : "))
if num % 2 == 0:
    print("Entered number is Even")
else:
    print("Entered number is Odd")

# Greatest of 3 numbers
num1 = int(input("a : "))
num2 = int(input("b : "))
num3 = int(input("c : "))
num4 = int(input("d : "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("a is greater")

elif num2 > num1 and num2 > num3 and num2 > num4:
    print("b is greater")

elif num3 > num1 and num3 > num2 and num3 > num4:
    print("c is greater")

else:
    print("d is greater")

# Multiple of 7
num = int(input("Enter a number : "))

if num % 7 == 0:
    print("Entered number is a multiple of 7")
else:
    print("Entered number is not a multiple of 7")
