# Basics 2 (Escape sequence, Concatenation, Functions, String Slicing, String Methods, Conditional Statements(IF,ELSE) )
# | Escape sequence > \n, \t | str ' ', " ", """ """ |
str1 = """ Hello there!, My Name is Sarmad \n Sarmad's age is 21 \n Fam: "Ali" """
print("1: ", str1)

# | Concatenation > str + str |
# | Functions > len(), type()
# | Indexing in python starts with 0 |
# | Slicing > str[ Starting_idx : Ending_idx ]
print("2: ", str1[1 : 13])
print("3: ", str1[1 : len(str1)])
print("4: ", str1[1 : ]) # [ 1 : the end]
print("5: ", str1[ 0 : 5 ]) # [ 0 : 5 ]

str = "I am a coder."

print(str.endswith("er.")) #returns true if string ends with substr
print(str.capitalize()) #capitalizes 1st char
print(str.replace("I am", "You are")) #replaces all occurrences of old
print(str.find("am")) #returns 1st index of 1st occurrer
print(str.count("am")) #counts the occurrence of substr

# Task time
name = input("Enter Your name: ")
print(len(name))

# Conditional Statements
# if-elif-else
age = 20

if (age >= 18):
    print("can vote")
    print("can drive")
elif (age < 18):
    print("can not vote")
else:
    print("can not vote")
    
#  in python, indentation is very importent (means spacing, as we did after condition before print)
# Example:

marks = int(input("Enter Your marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->", grade)

# Example 2:
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a > b and a >= c):
    print("first number is largest", a)
elif(b>= c):
    print("second number is largest", b)
else:
    print("third is largest", c)