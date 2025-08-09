# Functions and Recursion
# Funtion-----------------------------------------------------------------------------------------------------------------------------
# 1
# def CalcSum(a, b): 
#     sum = a + b
#     print(sum)
    
# CalcSum(65, 35)

# # 2
# def calcsum(a, b):
#     return a + b

# sum = calcsum(654654, 54864654)
# print(sum)

# # 3
# def phello():
#     print("Hello")
    
# save = phello()
# print(save)

# # 4
# def avg(a, b, c):
#     return (a+b+c)/3

# print(avg(7,7,7))

# Built-in Funtions and User define funtoins-----------------------------------------------
# Built-in > print(), len(), type(), range()
# User Define funtions

# 1
# cities = ["Ärifwala", "Sahiwal", "Lahore", "Burewala", "Multan"]

# def pc(list):
#     print(list)
    
# pc(cities)

# def pc1(list):
#     for c in list:
#         print(c, end = " ") # use end = " " , if we want to print in the same line

# pc1(cities)

# 2
# def fectorial(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i 
#     print("for loop: ", f)

# fectorial(6)

# def fectorial1(n):
#     f = 1
#     i = 1
#     while i <= n:
#         f *= i
#         i += 1
#     print("while loop: ", f)

# fectorial1(5)

# 3 - Convert usd to pkr
# def conv(x):
#     pkr = x*284.38
#     print(x,"USD =", pkr,"PKR")
    
# conv(5)

# 4
# def check(x):
#     if(x%2 == 0):
#         print("ËVEN")
#     elif(x%2 != 0):
#         print("ODD")
        
# x = int(input("ENter a number to check if it is even or odd: "))
# check(x)
        
# Recursion-----------------------------------------------------------------------------------------------------------------------------
# 1
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("WIN")

# show(5)

# 2
# def fectorial(x):
#     if (x == 0 or x ==1 ):
#         return 1
#     else:
#         # print(x)
#         return x * fectorial(x-1)
    
# print(fectorial(5))

# 3
def sumofN(n):
    sum = 0
    if(n == 0):
        return  
    
    sumofN(n-1) 
    sum += n
    return sum
    
print(sumofN(5))

# def sumofN(n):
#     if n == 0:
#         return 0
#     return n + sumofN(n - 1)

# print(sumofN(5))