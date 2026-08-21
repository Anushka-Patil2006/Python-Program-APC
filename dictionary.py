# 1. Student details and display all key-value pairs

student = {
    "roll_no": 101,
    "name": "Anushka",
    "department": "Computer Science",
    "marks": 95
}

for key, value in student.items():
    print(key, ":", value)


# 2. Employee information and display value of specified key

employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 55000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")


# 3. Dictionary of five products and prices, then add new product

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Tablet": 15000,
    "Keyboard": 1000,
    "Mouse": 500
}

products["Headphones"] = 2000

print(products)


# 4. Student marks and update specified student's marks

marks = {
    "Amit": 75,
    "Rahul": 80,
    "Sneha": 90,
    "Priya": 85
}

name = input("Enter student name: ")

if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")


# 5. Cities and populations, remove specified city

cities = {
    "Pune": 7000000,
    "Mumbai": 20000000,
    "Delhi": 19000000,
    "Kolhapur": 600000
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")


# 6. Employee IDs and names, check whether ID exists

employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")


# 7. Student records and total number of key-value pairs

students = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90,
    "Priya": 85
}

print("Total key-value pairs:", len(students))


# 8. Display all keys, values and key-value pairs

data = {
    "name": "Anushka",
    "age": 20,
    "course": "CSE",
    "marks": 85
}

print("Keys:", data.keys())
print("Values:", data.values())
print("Key-value pairs:", data.items())


# 9. Programming languages and their creators

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "JavaScript": "Brendan Eich"
}

for key, value in languages.items():
    print(key, ":", value)


# 10. Accept five student names and marks

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student dictionary:", students)


# 11. Student with highest marks

marks = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 95,
    "Priya": 82
}

highest_student = max(marks, key=marks.get)

print("Highest marks:", marks[highest_student])
print("Student:", highest_student)


# 12. Student with lowest marks

marks = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 95,
    "Priya": 62
}

lowest_student = min(marks, key=marks.get)

print("Lowest marks:", marks[lowest_student])
print("Student:", lowest_student)


# 13. Calculate average marks

marks = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 95,
    "Priya": 82
}

average = sum(marks.values()) / len(marks)

print("Average marks:", average)


# 14. Character frequency in a string

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:", frequency)


# 15. Word frequency in a sentence

sentence = input("Enter a sentence: ")

words = sentence.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


# 16. Merge two dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "d": 40,
    "e": 50,
    "f": 60
}

merged = {**dict1, **dict2}

print("Merged dictionary:", merged)


# 17. Find common keys in two dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common_keys = dict1.keys() & dict2.keys()

print("Common keys:", common_keys)


# 18. Find common values in two dictionaries

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 20,
    "y": 30,
    "z": 40
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:", common_values)


# 19. Remove duplicate values while retaining corresponding keys

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

unique_data = {}
seen = set()

for key, value in data.items():
    if value not in seen:
        unique_data[key] = value
        seen.add(value)

print("Dictionary after removing duplicate values:")
print(unique_data)


# 20. Display dictionary elements in ascending order of keys

data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

for key in sorted(data):
    print(key, ":", data[key])


# 21. Numbers from 1 to 10 and their squares

squares = {}

for i in range(1, 11):
    squares[i] = i ** 2

print(squares)


# 22. Even numbers from 1 to 20 and their squares

squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2

print(squares)


# 23. Unique numbers and their frequency

numbers = [1, 2, 3, 2, 4, 1, 3, 5, 2, 4]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Number frequency:", frequency)


# 24. Integers from 1 to 10 and their cubes

cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print(cubes)


# 25. Student management system

students = {
    "Amit": 75,
    "Rahul": 85,
    "Sneha": 92
}

# Add a student
name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks

# Update marks
name = input("Enter student name to update: ")

if name in students:
    students[name] = int(input("Enter new marks: "))

# Delete a student
name = input("Enter student name to delete: ")

if name in students:
    del students[name]

# Search for a student
name = input("Enter student name to search: ")

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

# Display all students
print("All students:", students)

# Find highest marks
if students:
    highest = max(students, key=students.get)
    print("Highest marks:", highest, students[highest])

# Calculate average
if students:
    average = sum(students.values()) / len(students)
    print("Average marks:", average)


# 26. Employee salaries

employees = {
    "Amit": 45000,
    "Rahul": 65000,
    "Sneha": 75000,
    "Priya": 40000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


# 27. Product quantity management

products = {
    "Laptop": 5,
    "Mobile": 15,
    "Keyboard": 8,
    "Mouse": 20
}

# Add product
name = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity

# Update quantity
name = input("Enter product to update: ")

if name in products:
    products[name] = int(input("Enter new quantity: "))

# Delete product
name = input("Enter product to delete: ")

if name in products:
    del products[name]

# Search product
name = input("Enter product to search: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

# Display products below quantity 10
print("Products with quantity below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, ":", quantity)


# 28. Contact management system

contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234"
}

# Add contact
name = input("Enter contact name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone

# Search contact
name = input("Enter contact name to search: ")

if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found")

# Update contact
name = input("Enter contact name to update: ")

if name in contacts:
    contacts[name] = input("Enter new phone number: ")

# Delete contact
name = input("Enter contact name to delete: ")

if name in contacts:
    del contacts[name]

# Display all contacts
print("All contacts:")

for name, phone in contacts.items():
    print(name, ":", phone)


# 29. Book management system

books = {
    101: "Python Programming",
    102: "Java Programming",
    103: "Data Science"
}

# Add a book
book_id = int(input("Enter book ID to add: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

# Search a book
book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")

# Remove a book
book_id = int(input("Enter book ID to remove: "))

if book_id in books:
    del books[book_id]

# Display all books
print("All books:")

for book_id, book_name in books.items():
    print(book_id, ":", book_name)

# Count total books
print("Total books:", len(books))


# 30. Group students according to department

students = {
    "Amit": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Rohan": "IT"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print("Students grouped by department:")

for department, names in departments.items():
    print(department, ":", names)


# 31. Group words according to their length

words = ["cat", "dog", "apple", "banana", "sun", "book"]

word_lengths = {}

for word in words:
    length = len(word)

    if length not in word_lengths:
        word_lengths[length] = []

    word_lengths[length].append(word)

print("Words grouped by length:")

for length, words_list in word_lengths.items():
    print(length, ":", words_list)


# 32. Find two numbers whose sum equals target using dictionary

numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

for num in numbers:
    required = target - num

    if required in seen:
        print("Two numbers:", required, num)
        break

    seen[num] = True


# 33. Find first character that occurs only once

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No unique character found")


# 34. Find first character that occurs more than once

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break
else:
    print("No repeating character found")


# 35. Word length and number of words having that length

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    length = len(word)
    length_count[length] = length_count.get(length, 0) + 1

print("Word length : Number of words")

for length, count in sorted(length_count.items()):
    print(length, ":", count)
