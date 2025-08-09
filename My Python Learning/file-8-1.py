# decorators and method types > static, class and object methods | property decorator
# 1. Normal Methods in classs/object's method-------------------------------------------------------------

# class person:
#     name = "anonymous"
#     def __init__(self, name):
#         self.name = name

#     def changeName(self, name):
#         self.name = name

# p = person("ALI")
# p.name =  "AHMAD"
# p.changeName("SARMAD")
# print(p.name)
# print(person.name)

# 2. class Methods/@classmethod---------------------------------------------------------------------------

# class person:
#     name = "anonymous"
#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p = person("ALI")
# p.name =  "AHMAD"
# p.changeName("SARMAD")
# print(p.name)
# print(person.name)

# 3. Static Methods/@staticmethod-------------------------------------------------------------------------

# class students:
#     school = "DPS" #class attribute
#     def __init__(self, name): # constructor
#         self.name = name # object attribute

#     @staticmethod # decorator
#     def Helo(): # static method   
#         print("Hello")

#     def welcom(self): # non-static/normal methods
#         print(f"Welcom, {self.name}!")
    
# s1 = students("Ahmad")
# s1.Helo()
# s1.welcom()

# s2 = students("Ali")
# s2.Helo()
# s2.welcom()

# 4. property method---------------------------------------------------------------------------------------

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property # this decorator used to define a method that can be accessed like an attribute
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student (98, 97, 99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)
# print(stu1.percentage()) # it will give error