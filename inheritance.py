#1.Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an additional attribute department. Display all employee and manager details and calculate the manager's annual salary.
class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,empid,name,salary,dept):
        super().__init__(empid,name,salary)
        self.dept=dept
    def display(self):
        print("emp id is:",self.empid)
        print("emp name:",self.name)
        print("Salary is:",self.salary)
        print("Dept is:",self.dept)
        self.a=self.salary*12
        print("annual income:",self.a)
m=Manager(101,"Sayali",200000,"IT")
m.display()
        
#2.	Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self,brand,model,fuel,prize):
        super().__init__(brand,model)
        self.fuel=fuel
        self.prize=prize
    def disp(self):
        print("Brand is:",self.brand)
        print("Model is:",self.model)
        print("fuel is:",self.fuel)
        print("prize is:",self.prize)

        self.d_p=self.prize-(self.prize*10/100)
        print("discount prize is:",self.d_p)
c=Car("BMW",12,"Petrol",6000000)
c.disp()
#3.	Create two classes Academic and Sports. The Academic class should store marks obtained by a student, while the Sports class should store sports points. Create a class Student that inherits from both classes and calculates the student's overall performance.
class Academic:
    def __init__(self,marks):
        self.marks=marks
class Sports:
    def __init__(self,sport_m):
        self.sport_m=sport_m
class Student(Academic,Sports):
    def __init__(self,marks,sport_m):
        Academic.__init__(self,marks)
        Sports.__init__(self,sport_m)
        self.total=self.marks+self.sport_m
    def Displayy(self):
        print("Academic marks are:",self.marks)
        print("Sports marks are:",self.sport_m)
        print("total marks are:",self.total)
s=Student(55,78)
s.Displayy()
    
    
#4.	Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create an Employee class that inherits from both classes and displays complete employee information.
class Personal_Details:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Professional_Details:
    def __init__(self,empid,designation,salary):
        self.empid=empid
        self.designation=designation
        self.salary=salary
class Employee(Personal_Details,Professional_Details):
    def __init__(self,name,age,empid,designation,salary):
        Personal_Details.__init__(self,name,age)
        Professional_Details.__init__(self,empid,designation,salary)

    def display(self):
        print("emp id is:",self.empid)
        print("name is:",self.name)
        print("age is:",self.age)
        print("designation is:",self.designation)
        print("Salary is:",self.salary)
e=Employee("Sayali",45,101,"HR",500000)
e.display()
    
    
#5.	Create a class Person containing name and age. Derive a class Student from Person with roll number and course. Further derive a class ResearchStudent from Student with research topic and guide name. Display all details.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,roll_no,course):
        Person.__init__(self,name,age)
        self.roll_no=roll_no
        self.course=course
class RStudent(Student):
    def __init__(self,name,age,roll_no,course,topic,guide):
        Student.__init__(self,name,age,roll_no,course)
        self.topic=topic
        self.guide=guide
    def disp(self):
        print("roll no is:",self.roll_no)
        print("Name is:",self.name)
        print("age is:",self.age)
        print("Course is:",self.course)
        print("topic is:",self.topic)
        print("guide is:",self.guide)
r=RStudent("sayali",45,67,"CSE","Healthcare"," Sonali Mam")
r.disp()
        
#6.	Create a base class BankAccount with account number and balance. Derive SavingsAccount from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, interest_rate):
        BankAccount.__init__(self, acc_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self.interest = self.balance * self.interest_rate / 100
        print("Interest is:", self.interest)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_no, balance, interest_rate, benefits):
        SavingsAccount.__init__(self, acc_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account number is:", self.acc_no)
        print("Balance is:", self.balance)
        print("Interest rate is:", self.interest_rate)
        print("Benefits are:", self.benefits)


p = PremiumSavingsAccount(101, 50000, 6, "Free Insurance")

p.calculate_interest()
p.display()

#7.	Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.
class Shape:
    def display(self):
        print("This is a shape")


class Circle(Shape):
    def area(self, r):
        a = 3.14 * r * r
        print("Area of Circle:", a)


class Rectangle(Shape):
    def area(self, l, b):
        a = l * b
        print("Area of Rectangle:", a)


class Triangle(Shape):
    def area(self, b, h):
        a = 0.5 * b * h
        print("Area of Triangle:", a)


c = Circle()
c.display()
c.area(5)

r = Rectangle()
r.display()
r.area(10, 5)

t = Triangle()
t.display()
t.area(8, 6)
        
    
#8.	Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.30
        salary = self.basic_salary + allowance
        print("Manager Salary:", salary)


class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.20
        salary = self.basic_salary + allowance
        print("Developer Salary:", salary)


class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.15
        salary = self.basic_salary + allowance
        print("Tester Salary:", salary)


m = Manager(101, "Rahul", 50000)
m.display()
m.calculate_salary()

d = Developer(102, "Amit", 40000)
d.display()
d.calculate_salary()

t = Tester(103, "Sneha", 35000)
t.display()
t.calculate_salary()

#9.	Create a class Person. Derive Student and Faculty from Person. Create another class TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate the use of multiple and hierarchical inheritance together.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no

    def display_student(self):
        print("Roll No:", self.roll_no)


class Faculty(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def display_faculty(self):
        print("Subject:", self.subject)


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        self.display_person()
        self.display_student()
        print("Subject:", self.subject)


ta = TeachingAssistant("Sayali", 21, 101, "Python")
ta.display()
#10.	Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_vehicle(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        print("Car Model:", self.model)


class Bike(Vehicle):
    def __init__(self, brand, engine):
        super().__init__(brand)
        self.engine = engine

    def display_bike(self):
        print("Engine:", self.engine, "cc")


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display_sports_car(self):
        print("Top Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, engine, battery):
        super().__init__(brand, engine)
        self.battery = battery

    def display_electric_bike(self):
        print("Battery:", self.battery, "kWh")


sc = SportsCar("BMW", "M4", 280)
sc.display_vehicle()
sc.display_car()
sc.display_sports_car()

print()

eb = ElectricBike("Ola", 0, 5)
eb.display_vehicle()
eb.display_bike()
eb.display_electric_bike()
#11.	Create a base class Student with attributes roll_no, name, and course. Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display_student(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


r = Result(101, "Sayali", "CSE", 80, 75, 90)

r.display_student()
r.calculate_result()
#12.	Create a class Product with product ID, name, and price. Derive ElectronicProduct with additional attributes such as brand and warranty. Calculate the final price after applying a discount.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def calculate_price(self, discount):
        final_price = self.price - (self.price * discount / 100)

        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")
        print("Discount:", discount, "%")
        print("Final Price:", final_price)


p = ElectronicProduct(101, "Laptop", 50000, "Dell", 2)

p.display_product()
p.calculate_price(10)
#13.	Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.
class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction Device supports printing and scanning")


m = MultifunctionDevice()

m.display()
m.print_document()
m.scan_document()
#14.	Create classes Camera and Phone. The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls. Create a Smartphone class inheriting from both.
class Camera:
    def take_photo(self):
        print("Taking photograph...")


class Phone:
    def make_call(self):
        print("Making phone call...")


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports camera and phone operations")


s = Smartphone()

s.display()
s.take_photo()
s.make_call()
#15.	Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display_research(self):
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


r = ResearchStudent( "Sayali", 21, 101, "CSE",
                    "Artificial Intelligence", "Dr. Patil")

r.display_person()
r.display_student()
r.display_research()
#16.	Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display_research(self):
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


r = ResearchStudent("Sayali", 21, 101, "CSE",
                    "Artificial Intelligence", "Dr. Patil")

r.display_person()
r.display_student()
r.display_research()

#17.	Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")

    def behavior(self):
        print("Dog is friendly")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

    def behavior(self):
        print("Cat is playful")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

    def behavior(self):
        print("Cow gives milk")


d = Dog("Tommy")
d.eat()
d.sound()
d.behavior()

print()

c = Cat("Kitty")
c.eat()
c.sound()
c.behavior()

print()

co = Cow("Gauri")
co.eat()
co.sound()
co.behavior()
#18.	Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        Person.__init__(self, name, age)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, age, disease):
        Person.__init__(self, name, age)
        self.disease = disease


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Doctor.__init__(self, name, age, specialization)
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)


s = Surgeon("Dr. Rahul", 40, "Cardiology", "Heart Disease")
s.display()
