# str and int can operate with *

print(3 * "#" * 2)

# str and str can operate with +

print(("2" + "@") * 3)

# Numeric values can operate with all arithmetic operators

print(2 + 3 * 4)

# Arithmetic expression with int and float will result in float

a = 10
b = 5.0
c = a * b
print(c)

# Result of division operator with 2 int will be float

a = 10
b = 5
c = a / b
print(c)

# integer division with float and int will give int displayed as float

a = 1.5
b = 3
c = a // b
print(c, a / b)

# floor gives closest integer, which is lesser than or equal to the float value. Result of a//b is same as floor(a/b).

