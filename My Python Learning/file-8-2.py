# Pilars of OOP
# 1. Abstraction----------------------------------------------------------------------------------------
# Import the ABC (Abstract Base Class) and abstractmethod decorator
from abc import ABC, abstractmethod

# Step 1: Create an abstract class named 'Vehicle'
# This class cannot be instantiated directly because it contains abstract methods
# class Vehicle(ABC):
#     # Step 2: Define an abstract method that subclasses must implement
#     @abstractmethod
#     def start_engine(self):
#         pass

#     # Abstract class can also have regular methods
#     def fuel_type(self):
#         print("This vehicle uses some form of fuel.")

# # Step 3: Create a concrete subclass 'Car' that inherits from Vehicle
# class Car(Vehicle):
#     # Must implement the abstract method 'start_engine'
#     def start_engine(self):
#         print("Car engine started! 🚗")

# # Step 4: Another subclass 'Motorcycle' also inherits from Vehicle
# class Motorcycle(Vehicle):
#     def start_engine(self):
#         print("Motorcycle engine roars to life! 🏍️")

# # Step 5: Instantiate and use the concrete classes
# # You cannot instantiate Vehicle directly as it has abstract methods
# car = Car()
# car.start_engine()     
# car.fuel_type()      

# bike = Motorcycle()
# bike.start_engine() 
# bike.fuel_type()    

# 2. Encapsulation-------------------------------------------------------------------------------------
# 1-------------------
# class Demo:
#     def __init__(self):
#         self.public = "public"
#         self._protected = "I'm protected"
#         self.__private = "I'm private"
#     def __hello(self):
#         print("Welcom", self.public)
#     def welcom(self):
#         self.__hello()

# obj = Demo()
# print(obj.public) 
# print(obj._protected)
# # print(obj.__private)   # AttributeError

# print(obj._Demo__private) 
# obj.welcom()

# 2-------------------
# class Account:
#     def __init__(self, blnc, accNo):
#         self.blnc = blnc
#         self.accNo = accNo

#     def debit(self, amount):
#         self.blnc -= amount
#         print(f"{amount}Rs. is debited!")

#     def credit(self, amount):
#         self.blnc += amount
#         print(f"{amount}Rs. is credited!")

#     def getBalance(self):
#         print(self.blnc) 
    
# acc1 = Account(10000, "Ac1")
# acc1.debit(500)
# acc1.getBalance( )

# acc2 = Account(1000, "Ac1")
# acc2.credit(500)
# acc2.getBalance()
# 2----------------
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner            # Public attribute: accessible from anywhere
#         self._account_type = "Saving" # Protected attribute: should be accessed only within class or subclass
#         self.__balance = balance      # Private attribute: not directly accessible outside the class

#     def show_account(self):
#         print(f"Owner: {self.owner}")
#         print(f"Account Type: {self._account_type}")
#         print(f"Balance: {self.__balance}")

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, amount):
#         if amount < 0:
#             print("Invalid amount. Balance cannot be negative.")
#         else:
#             self.__balance = amount

# account = BankAccount("Ali", 5000)
# print(account.owner) 
# print(account._account_type) 
# # print(account.__balance) 
# print(account.get_balance()) 

# account.set_balance(7000)
# print(account.get_balance()) 

# account.set_balance(-100)  

# account.show_account()

# 3. Inheritance-------------------------------------------------------------------------------------
# 1. single lvl,
# 2. multi lvl, 
# 3. multiple
# 4. super method 
# 1,2---------------------------------------
# Base class
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# # Derived class from Animal (single level inheritance)
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Derived class from Dog (multi-level inheritance)
# class Puppy(Dog):
#     def whine(self):
#         print("Puppy whines")


# p = Puppy()

# p.speak()   # Inherited from Animal
# p.bark()    # Inherited from Dog
# p.whine()   # Defined in Puppy
# 3-------------------------------------------
# First parent class
# class Flyable:
#     def fly(self):
#         print("Flying")

# # Second parent class
# class Swimmable:
#     def swim(self):
#         print("Swimming")

# # Child class inherits from both Flyable and Swimmable
# class Duck(Flyable, Swimmable):
#     def quack(self):
#         print("Quacking")

# d = Duck()

# d.fly()     # From Flyable
# d.swim()    # From Swimmable
# d.quack()   # Defined in Duck
# 4. super() method-----------------------------
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)

# 4. Polymorphisim-------------------------------------------------------------------------------------
# lets study dunder functions which is basicaly overloading of operators like +,-,/,*,%

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2): # it was a dunder method , cover the add with double underscore  
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex (newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2 #overloading in the iuse of +
num3.showNumber() 
