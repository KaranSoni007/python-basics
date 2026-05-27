# 1. Check if a number is:
# positive
# negative
# zero

num = int(input("Enter a number : "))
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")

# 2. Take a number and check:
# even or odd

num = int(input("Enter a number : "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# 3. Print numbers from 1 to 10 using a loop.

for i in range(1, 11):
    print(i)

# 4. Print all even numbers from 1 to 50.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 5. Print multiplication table of a number (e.g., 5).
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
