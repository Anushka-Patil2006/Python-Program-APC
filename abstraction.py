#1.	Create an abstract class Shape with an abstract method area(). Derive Circle, Rectangle, and Triangle classes and implement the area() method for each shape. Create objects of the derived classes and display their areas.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 4)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())
#2.	Create an abstract class Vehicle with abstract methods start() and stop(). Derive Car, Bike, and Bus classes and implement these methods.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")


vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()
    v.stop()
#3.	Create an abstract class BankAccount with abstract methods deposit() and withdraw(). Derive SavingsAccount and CurrentAccount and implement the required operations.
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Savings deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings withdrawal:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Current deposit:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Current withdrawal:", amount)


s = SavingsAccount(10000)
s.deposit(2000)
s.withdraw(3000)
print("Savings balance:", s.balance)

c = CurrentAccount(15000)
c.deposit(5000)
c.withdraw(4000)
print("Current balance:", c.balance)
#4.	Create an abstract class FoodOrder with abstract methods calculate_bill() and delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and implement the methods appropriately.
from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50


r = RestaurantOrder()
h = HomeDeliveryOrder()

print("Restaurant bill:", r.calculate_bill() + r.delivery_charge())
print("Home delivery bill:", h.calculate_bill() + h.delivery_charge())
#5.	Create an abstract class Patient with abstract methods calculate_bill() and treatment(). Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods according to the patient type.
from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment provided")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient treatment provided")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 8000

    def treatment(self):
        print("Emergency treatment provided")


patients = [InPatient(), OutPatient(), EmergencyPatient()]

for p in patients:
    p.treatment()
    print("Bill:", p.calculate_bill())
#6.	Create an abstract class Transport with an abstract method calculate_fare(distance). Implement subclasses:
#a)	Bus 
#b)	Train 
#c)	Taxi 
#d)	Flight 
#Calculate the fare according to the transportation type.
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 8


distance = 100

print("Bus fare:", Bus().calculate_fare(distance))
print("Train fare:", Train().calculate_fare(distance))
print("Taxi fare:", Taxi().calculate_fare(distance))
print("Flight fare:", Flight().calculate_fare(distance))
#7.	Create an abstract class Question with an abstract method evaluate_answer(). Derive:
#a)	MCQQuestion 
#b)	TrueFalseQuestion 
#c)	DescriptiveQuestion
#.Implement answer evaluation for each question type.
from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "B":
            return "Correct MCQ answer"
        return "Wrong MCQ answer"


class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "True":
            return "Correct True/False answer"
        return "Wrong True/False answer"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        if len(answer) > 20:
            return "Descriptive answer accepted"
        return "Descriptive answer is too short"


print(MCQQuestion().evaluate_answer("B"))
print(TrueFalseQuestion().evaluate_answer("True"))
print(DescriptiveQuestion().evaluate_answer(
    "Abstraction hides unnecessary details"
))
#8.	Create an abstract class Authentication with an abstract method authenticate(). Implement the method using:
#a)	Password authentication 
#b)	OTP authentication 
#c)	Biometric authentication 
#Demonstrate abstraction by interacting with objects through the abstract interface.
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.authenticate()
#9.	Create an abstract class CloudStorage with abstract methods:
#a)	upload_file() 
#b)	download_file() 
#c)	delete_file() 
#Create subclasses representing different storage services and implement the operations.
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")


storage = [GoogleDrive(), Dropbox()]

for s in storage:
    s.upload_file()
    s.download_file()
    s.delete_file()
#10.	Create an abstract class Appointment with abstract methods book_appointment() and calculate_fee(). Derive GeneralAppointment, SpecialistAppointment, and EmergencyAppointment.
from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for a in appointments:
    a.book_appointment()
    print("Fee:", a.calculate_fee())
