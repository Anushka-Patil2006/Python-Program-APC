#1.	Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.
class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    def display(self):
        self.per=(self.marks/100)*100
        print("Roll_no is:",self.roll_no)
        print("Name is:",self.name)
        print("Marks are:",self.marks)
        print("Percentage is:",self.per)
s1=Student(4,"sayali",90)
s2=Student(5,"Shreya",87)
s3=Student(6,"Deepali",75)
s1.display()
s2.display()
s3.display()

#2.	Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.
class Employee:
    def __init__(self,emp_id,name,bs):
        self.emp_id=emp_id
        self.name=name
        self.bs=bs
    def calc_HRA(self):
        self.HRA=self.bs*(20/100)
        print("HRA is:",self.HRA)
    def calc_DA(self):
        self.DA=self.bs*(10/100)
        print("Da is:",self.DA)
    def calc_gs(self):
        self.gs=self.HRA+self.DA+self.bs
        print("Gs is:",self.gs)
    def display(self):
        print("Emp id is:",self.emp_id)
        print("emp name:",self.name)
        print("basic sal:",self.bs)
e1=Employee(101,"Sayali",40000)
e1.display()
e1.calc_HRA()
e1.calc_DA()
e1.calc_gs()
        
#3.	Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        self.a=self.length*self.breadth
        print("area is:",self.a)
    def calc_peri(self):
        self.p=2*(self.length+self.breadth)
        print("Perimeter is:",self.p)
    def display(self):
        print("LEngth is:",self.length)
        print("BReadth is:",self.breadth)
r1=Rectangle(4,5)
r1.display()
r1.calc_area()
r1.calc_peri()
    
#4.	Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calc_area(self):
        self.ar=3.14*self.radius*self.radius
        print("area of circle is:",self.ar)
    def disp(self):
        print("radius is:",self.radius)
c1=Circle(7)
c1.disp()
c1.calc_area()
        
#5.	Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.
class Book:
    def __init__(self,book_id,title,author,price):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print("Book id is:",self.book_id)
        print("Title is:",self.title)
        print("Author is:",self.author)
        print("Price is:",self.price)
        print()

b1=Book(101,"Python","John",500)
b2=Book(102,"Java","James",600)
b3=Book(103,"C++","Dennis",700)

b1.display()
b2.display()
b3.display()
#6.	Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.
class ElectricityBill:
    def __init__(self,consumer_no,consumer_name,units):
        self.consumer_no=consumer_no
        self.consumer_name=consumer_name
        self.units=units

    def calc_bill(self):
        if self.units<=100:
            self.bill=self.units*5
        elif self.units<=200:
            self.bill=(100*5)+(self.units-100)*7
        else:
            self.bill=(100*5)+(100*7)+(self.units-200)*10

        print("Electricity bill is:",self.bill)

    def display(self):
        print("Consumer no is:",self.consumer_no)
        print("Consumer name is:",self.consumer_name)
        print("Units consumed:",self.units)

e1=ElectricityBill(101,"Sayali",250)
e1.display()
e1.calc_bill()
#7.	Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.
class MobilePhone:
    def __init__(self,brand,model,storage,price):
        self.brand=brand
        self.model=model
        self.storage=storage
        self.price=price

    def display(self):
        print("Brand is:",self.brand)
        print("Model is:",self.model)
        print("Storage is:",self.storage)
        print("Price is:",self.price)

    def discount(self):
        self.discount_price=self.price-(self.price*10/100)
        print("Price after discount is:",self.discount_price)

m1=MobilePhone("Samsung","A56","128GB",30000)
m1.display()
m1.discount()
#8.	Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.
class Patient:
    def __init__(self,patient_id,name,age,disease,fee):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.disease=disease
        self.fee=fee

    def display(self):
        print("Patient id is:",self.patient_id)
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Disease is:",self.disease)
        print("Consultation fee is:",self.fee)

    def total_bill(self):
        self.bill=self.fee
        print("Total bill is:",self.bill)

p1=Patient(101,"Sayali",21,"Fever",500)
p1.display()
p1.total_bill()
#9.	Design an ATM class that allows a user to:
#a)	Check balance 
#b)	Deposit money 
#c)	Withdraw money 
#d)	Display account details
#Create an object of the class and implement the operations through a menu-driven program.
class ATM:
    def __init__(self,account_no,name,balance):
        self.account_no=account_no
        self.name=name
        self.balance=balance

    def check_balance(self):
        print("Balance is:",self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited:",amount)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Amount withdrawn:",amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account no is:",self.account_no)
        print("Name is:",self.name)
        print("Balance is:",self.balance)


a1=ATM(12345,"Sayali",10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Account Details")
    print("5. Exit")

    ch=int(input("Enter your choice:"))

    if ch==1:
        a1.check_balance()
    elif ch==2:
        amount=int(input("Enter amount:"))
        a1.deposit(amount)
    elif ch==3:
        amount=int(input("Enter amount:"))
        a1.withdraw(amount)
    elif ch==4:
        a1.display()
    elif ch==5:
        break
    else:
        print("Invalid choice")
#10.	Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.
class Vehicle:
    def __init__(self,vehicle_no,model,rate,availability):
        self.vehicle_no=vehicle_no
        self.model=model
        self.rate=rate
        self.availability=availability

    def rent(self,days):
        if self.availability:
            self.charges=self.rate*days
            self.availability=False
            print("Vehicle rented successfully")
            print("Rental charges:",self.charges)
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability=True
        print("Vehicle returned successfully")

v1=Vehicle("MH09AB1234","Swift",1500,True)

v1.rent(3)
v1.return_vehicle()
#11.	Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.
class ShoppingCart:
    def __init__(self,name,cart_id):
        self.name=name
        self.cart_id=cart_id
        self.products=[]

    def add_product(self,product,price):
        self.products.append([product,price])
        print("Product added")

    def remove_product(self,product):
        for p in self.products:
            if p[0]==product:
                self.products.remove(p)
                print("Product removed")
                return
        print("Product not found")

    def total_bill(self):
        total=0
        for p in self.products:
            total=total+p[1]
        print("Total bill is:",total)

    def __del__(self):
        print("Shopping cart destroyed")

c1=ShoppingCart("Sayali",101)

c1.add_product("Book",500)
c1.add_product("Pen",50)

c1.total_bill()
c1.remove_product("Pen")
c1.total_bill()
#12.	Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.
class FoodOrder:
    def __init__(self,order_id,name,food,quantity,price):
        self.order_id=order_id
        self.name=name
        self.food=food
        self.quantity=quantity
        self.price=price

    def total_bill(self):
        self.total=self.quantity*self.price
        self.tax=self.total*5/100
        self.bill=self.total+self.tax
        print("Total bill including tax is:",self.bill)

    def display(self):
        print("Order id is:",self.order_id)
        print("Customer name is:",self.name)
        print("Food item is:",self.food)
        print("Quantity is:",self.quantity)
        print("Price is:",self.price)

    def __del__(self):
        print("Order completed")

f1=FoodOrder(101,"Sayali","Pizza",2,300)

f1.display()
f1.total_bill()
#13.	Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.
class StudentResult:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5

    def total(self):
        self.t=self.m1+self.m2+self.m3+self.m4+self.m5
        print("Total marks are:",self.t)

    def percentage(self):
        self.per=(self.t/500)*100
        print("Percentage is:",self.per)

    def grade(self):
        if self.per>=75:
            print("Grade is: A")
        elif self.per>=60:
            print("Grade is: B")
        elif self.per>=50:
            print("Grade is: C")
        elif self.per>=40:
            print("Grade is: D")
        else:
            print("Fail")

    def __del__(self):
        print("Student result object destroyed")


s1=StudentResult("Sayali",80,75,90,85,70)

print("Name is:",s1.name)
s1.total()
s1.percentage()
s1.grade()
