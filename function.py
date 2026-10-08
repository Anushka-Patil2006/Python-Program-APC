# 1. Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter number: "))
print("Factorial =", factorial(n))


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(check_even_odd(n))


# 3. Define a function that accepts two numbers and returns the greater number.

def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number =", greater(a, b))


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))


# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter number: "))
print(is_prime(n))


# 6. Define a function to calculate the area of a circle using its radius.

def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area =", area_circle(r))


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.

def sum_natural(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))
print("Sum =", sum_natural(n))


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.

def power(base, exponent):
    return base ** exponent

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Answer =", power(base, exponent))


# 9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def largest(numbers):
    large = numbers[0]

    for n in numbers:
        if n > large:
            large = n

    return large

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))


# 10. Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(s):
    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

s = input("Enter string: ")
print("Number of vowels =", count_vowels(s))


# 11. Write a function that accepts a string and returns its reverse.

def reverse_string(s):
    return s[::-1]

s = input("Enter string: ")
print("Reverse =", reverse_string(s))


# 12. Create a function that checks whether a given string or number is a palindrome.

def palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False

value = input("Enter string or number: ")
print(palindrome(value))


# 13. Write a function that accepts a list of numbers and returns their average.

def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Average =", average(numbers))


# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count = count + 1

    return count

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))
print("Count =", count_element(numbers, element))


# 15. Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(numbers):
    unique = []

    for n in numbers:
        if n not in unique:
            unique.append(n)

    return unique

numbers = list(map(int, input("Enter numbers: ").split()))
print("Unique elements =", unique_elements(numbers))


# 16. Create a function to find the second-largest number in a list.

def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(numbers))


# 17. Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))
print("Fibonacci =", fibonacci(n))


# 18. Create a function that accepts marks in five subjects and returns the student's percentage and grade.

def calculate_grade(marks):
    percentage = sum(marks) / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = calculate_grade(marks)

print("Percentage =", percentage)
print("Grade =", grade)


# 19. Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.

def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter units: "))
print("Electricity Bill =", electricity_bill(units))


# 20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))


# 21. Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount = total * 0.10

    return total - discount

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

print("Total Bill =", total_bill(prices, quantities))


# 22. Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, average = calculate(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)


# 23. Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    marks = []

    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total = total_marks(marks)
    percent = percentage(marks)
    g = grade(percent)

    students.append([name, roll, total, percent, g])

for student in students:
    print(student)

class_average = sum(student[3] for student in students) / n

highest = max(students, key=lambda x: x[3])
lowest = min(students, key=lambda x: x[3])

print("Class Average =", class_average)
print("Highest Scorer =", highest[0])
print("Lowest Scorer =", lowest[0])


# 24. Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.

balance = 0
transactions = []

def deposit(amount):
    global balance
    balance = balance + amount
    transactions.append("Deposited " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")

def balance_enquiry():
    print("Balance =", balance)

def transaction_history():
    print("Transactions:")
    for t in transactions:
        print(t)

deposit(5000)
withdrawal(1000)
balance_enquiry()
transaction_history()


# 25. Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.

books = {}

def add_book(name):
    books[name] = True

def issue_book(name):
    if name in books and books[name]:
        books[name] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(name):
    if name in books:
        books[name] = True
        print("Book returned")

def search_book(name):
    if name in books:
        print("Book found")
    else:
        print("Book not found")

def display_books():
    for name in books:
        if books[name]:
            print(name)

add_book("Python")
add_book("Java")
add_book("C++")

issue_book("Python")
return_book("Python")
search_book("Java")

print("Available Books:")
display_books()


# 33. Write a lambda function to calculate the square of a given number.

square = lambda x: x * x

n = int(input("Enter number: "))
print("Square =", square(n))


# 34. Create a lambda function that returns the cube of a number.

cube = lambda x: x * x * x

n = int(input("Enter number: "))
print("Cube =", cube(n))


# 35. Write a lambda function that returns True if a number is even and False otherwise.

even = lambda x: x % 2 == 0

n = int(input("Enter number: "))
print(even(n))


# 36. Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))


# 37. Create a lambda function to calculate simple interest using principal, rate, and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))


# 38. Take a list of numbers, use map() and a lambda function to generate a list containing their squares.

numbers = list(map(int, input("Enter numbers: ").split()))

squares = list(map(lambda x: x * x, numbers))

print("Squares =", squares)


# 39. Use map() with lambda to calculate the cube of every element in a list.

numbers = list(map(int, input("Enter numbers: ").split()))

cubes = list(map(lambda x: x * x * x, numbers))

print("Cubes =", cubes)


# 40. Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda x, y: x + y, list1, list2))

print("Result =", result)


# 41. Take a list of integers, use filter() and lambda to extract all even numbers.

numbers = list(map(int, input("Enter numbers: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers =", even_numbers)


# 42. Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.

def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = list(map(int, input("Enter numbers: ").split()))

prime_numbers = list(filter(lambda x: is_prime_number(x), numbers))

print("Prime numbers =", prime_numbers)


# 43. Use filter() and lambda to extract positive numbers from a list.

numbers = list(map(int, input("Enter numbers: ").split()))

positive = list(filter(lambda x: x > 0, numbers))

print("Positive numbers =", positive)


# 44. Take a list of numbers, use filter() and lambda to find numbers greater than 50.

numbers = list(map(int, input("Enter numbers: ").split()))

greater = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50 =", greater)


# 45. Take a list of words, use filter() and lambda to find words having more than five characters.

words = input("Enter words: ").split()

result = list(filter(lambda word: len(word) > 5, words))

print("Words =", result)


# 46. Take a list of words; sort them according to their length using lambda.

words = input("Enter words: ").split()

words.sort(key=lambda word: len(word))

print("Sorted words =", words)


# 47. Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.

students = [
    ("Anushka", 85),
    ("Riya", 70),
    ("Sneha", 92),
    ("Priya", 78)
]

students.sort(key=lambda x: x[1])

print("Students sorted by marks:")
for student in students:
    print(student)


# 48. Take employee records containing name and salary, sort them according to salary using lambda.

employees = [
    ("Amit", 40000),
    ("Rahul", 60000),
    ("Sneha", 50000),
    ("Priya", 70000)
]

employees.sort(key=lambda x: x[1])

print("Employees sorted by salary:")
for employee in employees:
    print(employee)


# 49. Take a list containing student names and marks, use functions and lambda expressions to calculate average marks, filter students scoring above 75, and sort students according to marks.

students = [
    ("Anushka", 85),
    ("Riya", 70),
    ("Sneha", 92),
    ("Priya", 78)
]

def average_marks(students):
    total = sum(mark for name, mark in students)
    return total / len(students)

above_75 = list(filter(lambda x: x[1] > 75, students))

sorted_students = sorted(students, key=lambda x: x[1])

print("Average Marks =", average_marks(students))
print("Students above 75 =", above_75)
print("Sorted Students =", sorted_students)


# 50. Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to find employees earning more than ₹50,000, increase salaries by 10%, and sort employees according to salary.

employees = [
    ("Amit", "IT", 45000),
    ("Rahul", "HR", 60000),
    ("Sneha", "IT", 75000),
    ("Priya", "Sales", 50000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

increased_salary = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))

sorted_employees = sorted(employees, key=lambda x: x[2])

print("Employees earning more than 50000:")
print(high_salary)

print("Salaries after 10% increase:")
print(increased_salary)

print("Employees sorted by salary:")
print(sorted_employees)


# 51. Take a list of products with names, prices, and quantities, use functions and lambda expressions to calculate total value of each product, filter products costing more than ₹1,000, and sort products according to total value.

products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 10000, 1)
]

def total_value(product):
    return product[1] * product[2]

values = list(map(lambda x: (x[0], total_value(x)), products))

above_1000 = list(filter(lambda x: x[1] > 1000, values))

sorted_products = sorted(values, key=lambda x: x[1])

print("Total value:")
print(values)

print("Products above 1000:")
print(above_1000)

print("Products sorted by total value:")
print(sorted_products)
