# List and Tuples
# list / arrays----------------------------------------------------------------------------------------------------------------------
marks = [50,45,65,54] 
print(type(marks))
print(marks)
print(marks[2])
# print(marks[5]) #  list index out of range

abc = ["Sarmad", 21, 1505.321] # we can store any type of data
abc[0] = "Sarmad Rj" # list is mutable
print(abc)

# List slicing same as strings (SubList)------------------------------
# List Methods--------------------------------------------------------
# append, sort, reverse, insert, remove, pop
list = [4,2,3,1]
list.append(5)
# print(list.append(5))
print(list.sort()) # or list.sort(reverse=True)
print(list)

list2 = ['a', 'd', 'x' , 'j', 'z', 'c']
list2.insert(2, 'b') # .insert(indx, value)
list2.sort(reverse=True) 
print(list2)


list3 = [5,3,4,2,1]
list3.reverse() # nor same as sorting 
print(list3)

list4 = [2, 1 ,3, 1, 3]
list4.remove(3) # .remove(value you want to remove) , it will only remove the first value
print(list4)
list4.pop(2) # .pop(index) > it will remove the value on the given index
print(list4)


# tuples -----------------------------------------------------------------------------------------------------------------------------
tup = ()
print(type(tup))

tup1 = (54, 35, 54)
# tup1[0] = 54  # it is immutable, 'tuple' object does not support item assignment

tup2 = (1)
print(type(tup2))
tup3 = (1,)
print(type(tup3))

# slicing in tuple is same as list and string 
# Methods
# index, count
print(tup1.index(54))
print(tup1.count(54))

# Task -----------------------------------------------------------------------------------------------------------------------------

# movies = []

# movies.append(input("Enter the first movie name: "))
# movies.append(input("Enter the second movie name: "))
# movies.append(input("Enter the third movie name: "))

# print(movies)

x = [1, 2, 3, 2, 1]
y = x.copy()

y.reverse()

print(x)
print(y)


if(x == y):
    print("list is palindrome")
else:
    print("list is not palindrome")