# Loops > for, while
# while--------------------------------------------------------------------------------------------------------------------------------

# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# while x <= 10:
#     print("abc", x)
#     x += 1

# list = [1, 4 , 5, 9, 15, 42 ,25]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1
    
# x = 1
# while x <= 10:
#     print(x)
#     if (x == 5):
#         break
    
#     x += 1
    
# x = 1
# while x <= 10:
#     print(x)
#     if (x == 5):
#         continue
#     x += 1

# for--------------------------------------------------------------------------------------------------------------------------------

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(type(list))
# list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# print(type(list))

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# tup = (12, 13, 14, 15, 16, 17, 18, 19, 20)

# for x in list:
#     print(x)
    
# for x in tup:
#     print(x)
# else:
#     print("END") #else wont work if we break the loop
    
# str = "hello i am sarmad!!"
# for x in str:
#     print(x)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49
# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#     idx += 1

# range()------------------------------------------------------------------------
# print(range(5))

# sequence = range(5) 
# print(sequence)
# print(sequence[0])
# print(sequence[1])
# print(sequence[2])
# print(sequence[3])
# print(sequence[4])
# print(sequence[5]) # it will throw error bcz of index

# we can use loop

# for x in range(10): # range(stop)
#     print(x)
    
# for x in range(1, 20): # range(start, stop)
#     print(x)
    
# for x in range(5, 21, 5): # range(start, stop, step)
#     print(x)
    
# for x in range(10, 0, -1):
#     print(x)

# pass statement------------------------------------------------------------------------

for i in range(20):
    pass

if(i > 5):
    pass

# pass means abhi koi kaam nhi krwana bad main kabhi koi kaam krwa lenge, usualy use in try catch

# Task--------------------------------------------------------------------------------------------------------------------------------
# x = int(input("Enter the number for table: "))

# for i in range(1, 11):
#     print(x, "x", i, "=", i*x)

# x = 5
# for i in range(1, 11):
#     print(f"{x} x {i} = {x*i}")