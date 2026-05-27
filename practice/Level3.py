# 1. Find the sum of first 100 numbers
total = 0
for i in range(1, 101):
    total = total + i
print("Sum:", total)

# 2. Count how many numbers from 1–100 are divisible by 3

for i in range(1, 100):
    if i%3 == 0:
        print(i)

# 3. Reverse a number
# Example:
# Input: 1234
# Output: 4321

num = input("Enter a number: ")
rev = num[::-1]
print("Reversed:", rev)

# 4. Find the largest number in a list:
list1 = [10, 45, 2, 99, 23]
largest = list1[0]
for i in list1:
    if i>largest:
        largest = i
print("Largest number:", largest)


# 5. Count vowels in a string
# Example:
# "hello world" → 3

text = input("Enter a string: ")
count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)
