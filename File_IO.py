# f = open("demo.txt", "r")
# # data = f.read()
# # print(data)
# # print(type(data))

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

# ==>
# f = open("demo.txt", "a")
# f.write("\nTomorrow, i will start introduction of OOPS\nThen day after tomorrow, I will start building a mini-project")
# f.close()


# ==> r+ is a file reading and overwrite character used for file reading and overwriting the text from starting, as the pointer points at starting of text

# ==> w+ has same purpose like r+, but there is a difference. In r+, there is no truncation takes place, and in w+ truncation of data must takes place.

# ==> a+ is used to read and append data having pointer at end, and no truncate of data

# ==> With statement
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

with open("demo.txt", "w") as f:
    f.write("new data")

# when we are using with statement, then there is no need to close the file, as it is done automatically.

# import os
# os.remove("demo.txt")
# the above command is used to delete file permanently from the system