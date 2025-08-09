# File I/O--------------------------------------------------------------------------------
# file = open("abc.txt", "r")
# r = file.read() # read entire file
# line1 = file.readline() # read one line -----------------------------
# line2 = file.readline() # read one line -----------------------------
# # print(type(r))
# print(r) 
# print(line1)
# print(line2)
# file.close()

# with open("jango.txt", "a+") as f: # with syntex-----------------------
#     f.write("\nabc1")
#     r =  f.read() 
#     print(r)


#  to remove a file / delete-------------------------------------------
# file = open("sarmad.txt", "a+")
# a = file.write("helo")
import os
# os.remove("sarmad")

# task------------------------------------------------------------------------------------------
# with open("practice.txt", "a+") as f:
#     f.write("Hi Everyone")
#     f.write("\nwe are learning File i/o")
#     f.write("\nusing Java")
#     f.write("\nI like programming in Java\n")
    
# with open("practice.txt", "r") as r:
#     data = r.read()
#     print(data)

# nd = data.replace("Java", "Python")
# print(nd)

# with open("practice.txt", "w") as f:
#     f.write(nd)

# 2
# find learning
# with open("practice.txt", "r") as r:
#     data = r.read()

# if(data.find("learning") != -1): # or "learning" in data
#     print("found")
# else:
#     print("not found")

# 3
# def check_the_line(word):
#     data = True
#     lineNo = 1
#     with open("practice.txt", "r") as r:
#         while data:
#             data = r.readline()
#             if(word in data):
#                 print(lineNo)
#                 return
#             lineNo += 1
#     return -1

# print(check_the_line("sarmad"))
# print(check_the_line("learning"))

# 4
with open("practice1.txt", "r") as f:
    data = f.read()
    nums = data.split(", ")
    count = 0
    for value in nums:
        if(int(value) % 2 == 0):
            count += 1
    print(count)
    


day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")