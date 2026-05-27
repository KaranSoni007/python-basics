# Traffic Light using if-elif-else
light = input("color : ")

if light == "red":
    print("Stop")

elif light == "yellow":
    print("Wait")

elif light == "green":
    print("Let's Go")

else:
    print("Invalid Color")


# Student Grading System
marks = int(input("Marks : "))

if marks > 80:
    print("Invalid Marks")

elif marks >= 70 and marks <= 80:
    print("Grade A")

elif marks >= 60 and marks <= 70:
    print("Grade B")

elif marks >= 50 and marks <= 60:
    print("Grade C")

elif marks >= 40 and marks <= 50:
    print("Grade D")

else:
    print("Fail")

# Condition in one line
food = input("Food : ")
print("sweet") if food == "cake" or food == "ice cream" else print("not sweet")
