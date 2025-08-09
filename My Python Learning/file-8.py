# class and object and constructors, MY CGPA CALCULATOR & del keyword -------------------------------------------------------------------------------------------
# Class and Object------------------------------------------------------------------------------
# # 1------------
# class student: # class
#     name = "ali"

# s1 = student() # object/ instace
# print(s1.name)

# # 2------------
# class car:
#     color = "Blue"
#     brand = "mercedes"

# car1 = car()
# print(car1.color)
# print(car1.brand)

# Constructor---------------------------------------
# # 1-----------
# class student:
#     schoolName = "DPS" # class attribute
#     def __init__(self, p_name, p_age): # Constructor, where self is basically mean we are giving our obj name as self, but we must write refrence (to the object)
#         self.name = p_name # object attribute
#         self.age = p_age
#     def welcome(self): # self is must
#         print("Welcome", self.name)
#     def getAge(self):
#         return self.age
# s1 = student("sarmad", 21)
# print("Student name:",s1.name)
# print("Student age:", s1.age)
# s1.name = "SARMAD RJ"
# s1.welcome()
# print("Age is:", s1.getAge())

# # 2-----------
# class car:
#     def __init__(self): # Default Constructor 
#         pass

#     def __init__(self, color): # parameterized Constructor
#         self.color = color

# Task-----------------------------------------------------------------------------------------------------
# CGPA Calculator
# total_semesters = int(input("Enter the value of Your total semesters: "))
# print("Now enter Your GPA of each semster one by one!")
# GPAs = []
# for i in range(total_semesters):
#     GPAs.append(float(input(f"Enter GPA of Semester {i+1}: ")))
# CGPA = 0
# for i in range(len(GPAs)):
#     CGPA += GPAs[i]

# CGPA /= total_semesters
# print("Your CGPA is", CGPA)

# now lets convert it into what I learned now---------------------------
class CGPA_CALC:
    def __init__(self, sems, GPAs):
        self.sems = sems
        self.GPAs = GPAs

    def calc(self):
        CGPA = 0
        for i in range(len(self.GPAs)):
            CGPA += GPAs[i]
        CGPA /= self.sems
        print("Your CGPA is", CGPA)
    

total_semesters = int(input("Enter the value of Your total semesters: "))
print("Now enter Your GPA of each semster one by one!")
GPAs = []
for i in range(total_semesters):
    GPAs.append(float(input(f"Enter GPA of Semester {i+1}: ")))

try1 = CGPA_CALC(total_semesters, GPAs)
try1.calc()



# delete keyword!-----------------------------------------------------------------------------------
# used to delete the instance/obj ot its properties
# class student:
#     name = ""
#     def __init__(self, age):
#         self.age = age

# s1 = student(21)
# s1.name = "ali"
# print(s1.name)
# print(s1.age)
# del s1.name
# del s1.age
# print(s1.name) # no error, bcz not object's attribute
# print(s1.age) # error

# del s1 # delete the complete obj


# using class name in the constructor-----------------------------------------------------------------------
# class person1:
#     name = "anonymous"
#     def __init__(self, name):
#         self.name = name

# class person2:
#     name = "anonymous"
#     def __init__(self, name):
#         self.name = name
#         person2.name = name 
#         # self.__class__.name = name # or the uper line
# # 1
# p1 = person1("ali")
# print(person1.name)
# print(p1.name)
# p1.name = "Sarmad"
# print(p1.name)
# # 2
# p2 = person2("ahmad")
# print(person2.name)
# print(p2.name)
# p2.name = "Sarmad"
# print(p2.name)