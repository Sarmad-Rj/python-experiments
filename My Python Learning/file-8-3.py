#  some task at the end....
# 1---------------------------------------------------------------------
class circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        Area = (22/7) * self.radius ** 2
        return Area
    
    def Peri(self):
        Peri =  2 * (22/7) * self.radius
        return Peri   

c1 = circle(21)
print(c1.Area())
print(c1.Peri())

# 2---------------------------------------------------------------------
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept 
        self.salary = salary

    def showdetails(self):
        print("Role =", self.role)
        print("Department =", self.dept)
        print("Salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        super().__init__("Engineer", "IT", "20,000")

    def showdetails(self):
        print("Name =", self.name)
        print("Age =", self.age)
        super().showdetails()

eng = Engineer("Ali", 21)
eng.showdetails()

# 3---------------------------------------------------------------------
class order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price  

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = order("chips", 100)
odr2 = order("tea", 70)
print(odr1 > odr2)





# anddddd



class order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price  # in this solution we can just self.price = int(price) 

    
odr1 = order("chips", 100)
odr2 = order("tea", "70")

print(odr1.price)
print(odr2.price)

