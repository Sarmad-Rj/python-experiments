# Dictionary & Set
# Dictionary-----------------------------------------------------------------------------------------------------------------------------
MyInfo = {
    "name" : "SARMAD", # no error but wont exicute/print
    "age" : 20,
    "name" : "SARMAD RJ", # overrite
    "roll no" : 15,
    "subjects" : ["OOP", "DB", "IT"],
    "Topics" : ("inheritance", "TRC, DRC", 51),
    "CGPA" : 3.12 
} # no index, mutable, no duplicate value cuz it will overrite

print(type(MyInfo))
print(MyInfo)
print(MyInfo["name"])
MyInfo["age"] = 21 # reassign
MyInfo["father name"] = "Liaqat Ali" # add a new key
print(MyInfo)

# Nested Dictionary-----------------------------------------------------------
student = {
    "name" : "Ali",
    "age" : 15,
    "marks" : {
        "math" : 95,
        "eng" : 99,
        "urdu": 90
    }
}
address = {
    "city" : "Arifwala",
    "zipCode" : 354135
}
print(student)
print(student["marks"])
print(student["marks"]["math"])

# Dictionary's methods-----------------------------------------------------------

print(student.keys()) # return the keys in dict
print(student.values()) # return the values
print(student.items()) # return the key and value int the formate of tuple
print(student.get("name")) # return the value of given key in dict
student.update(address)
print(student) # add the values of other dict / besides it is also used when we have to add multiple keys
student.update({"Roll No": 15})


# besides method we can also..
print(list(student.keys())) # make the list of keys in dict
print(len(list(student.keys()))) # return the length

# EXPLAINATION OF ERROR
# print("BEFORE")
# print(student["name1"]) # this way will throw error, but if we use get method that will return none
# print("AFTER")

# Sets-----------------------------------------------------------------------------------------------------------------------------
dict = {} #syntax of an empty Dictionary
print(type(dict))

set = {1, 3}  # mutable, values in it are immutable, only value, ignores duplicate values, unordered 
print(type(set))

# set1 = set() #syntax of an empty set
# print(type(set1))

set2 = {3, 2, 2, 5, "SARMAD", "HELLO", 1}
print(set2) # returns {1, 2, 3, 'SARMAD', 5, 'HELLO'} or {'HELLO', 2, 3, 'SARMAD', 5, 1}, mean totaly diff order...

# Set's methods-----------------------------------------------------------
# add, remove, clear pop

set.add(2)
set.add("abc")

set.remove(1)
print(set)

print(set.pop()) #pick random value

print(set.union(set2))
print(set.intersection(set2))

set.clear()
print(set)

# Task-----------------------------------------------------------------------------------------------------------------------------
# marks = {}

# a = int(input("Enter Your makrs of subject Math: "))
# b = int(input("Enter Your makrs of subject English: "))
# c = int(input("Enter Your makrs of subject Science: "))

# marks.update({"Math": a})
# marks.update({"English": b})
# marks.update({"Science": c})

# print(marks)
