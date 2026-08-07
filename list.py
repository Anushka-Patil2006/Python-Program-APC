#1.Write a Python program to create a list of five fruits and display the list.

l1=["Apple","Banana","Watermelon","Mango","Grape"]
print(l1)

#2. Create a list of five integers. Display: First element Last element Third element
l1=[10,20,30,40,50]
print("First Element: ",l1[0])
print("Second Element: ",l1[1])
print("Third Element: ",l1[2])

# 3.Create a list of colors. Replace the third color with another color and display the updated list.
colors = ["Red", "Blue", "Green", "Yellow", "Black"]

colors[2] = "Pink"

print("Updated List:", colors)


# Q4. Create a list of numbers. Add:
# 1) One element at the end
# 2) One element at the beginning
# 3) One element at a specified position

numbers = [10, 20, 30, 40]

numbers.append(50)          # End
numbers.insert(0, 5)        # Beginning
numbers.insert(3, 25)       # Position

print("Updated List:", numbers)

#Q5. Create a list of student names. Remove:
# 1) First student
# 2) Last student
# 3) A specific student by name
students = ["Amit", "Riya", "Sneha", "Rahul", "Pooja"]

students.pop(0)
students.pop()
students.remove("Sneha")

print("Remaining Students:", students)



# Q6. Find the largest and smallest number in a list
# without using max() or min().

numbers = [25, 10, 45, 5, 90, 30]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest Number:", largest)
print("Smallest Number:", smallest)


# Q7. Accept 10 numbers from the user and store them in a list.
# Calculate Sum and Average.

numbers = []

for i in range(10):
    num = int(input("Enter Number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", average)


# Q8. Store 15 integers in a list.
# Count Even and Odd numbers.

numbers = []

for i in range(15):
    num = int(input("Enter Number: "))
    numbers.append(num)

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)


# Q9. Create a list of cities. Ask the user to enter a city
# name and check whether it exists in the list.

cities = ["Pune", "Mumbai", "Kolhapur", "Satara", "Nashik"]

city = input("Enter City Name: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")


# Q10. Write a program to reverse a list without using
# reverse() method.

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Original List:", numbers)
print("Reversed List:", reversed_list)

# Q11. Create a list of 10 numbers and display:
# First 5 elements, Last 5 elements, Middle 4 elements,
# Alternate elements, Reverse list using slicing.

numbers = [10,20,30,40,50,60,70,80,90,100]

print("First 5 Elements :", numbers[:5])
print("Last 5 Elements :", numbers[5:])
print("Middle 4 Elements :", numbers[3:7])
print("Alternate Elements :", numbers[::2])
print("Reverse List :", numbers[::-1])


# Q12. Display all elements present at even index positions.

numbers = [10,20,30,40,50,60,70,80]

print("Elements at Even Index Positions:")

for i in range(0, len(numbers), 2):
    print(numbers[i])



# Q13. Accept 10 numbers and sort them in
# Ascending and Descending order.

numbers = []

for i in range(10):
    num = int(input("Enter Number: "))
    numbers.append(num)

asc = sorted(numbers)
desc = sorted(numbers, reverse=True)

print("Ascending Order :", asc)
print("Descending Order :", desc)


# Q14. Create a list containing duplicate values and display
# only unique elements.

numbers = [10,20,30,20,40,50,30,60,10]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Unique Elements :", unique)


# Q15. Find the second largest element in a list.

numbers = [10,45,67,89,23,56]

numbers.sort()

print("Second Largest Element :", numbers[-2])


# Q16. Create a nested list storing:
# Student Name, Roll Number and Marks.
# Display all student details.

students = [
    ["Amit", 101, 85],
    ["Sneha", 102, 90],
    ["Rahul", 103, 78]
]

print("Student Details")

for i in students:
    print("Name :", i[0])
    print("Roll No :", i[1])
    print("Marks :", i[2])
    print()


# Q17. Create two 3×3 matrices using nested lists and
# perform matrix addition.

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Matrix Addition:")

for row in result:
    print(row)


# Q18. Create a shopping cart using a list.
# Perform Add, Remove, Search, Display and Count.

cart = ["Milk", "Bread", "Sugar"]

cart.append("Tea")             # Add
cart.remove("Bread")           # Remove

item = "Milk"

if item in cart:
    print(item, "Found in Cart")
else:
    print(item, "Not Found")

print("Shopping Cart :", cart)
print("Total Items :", len(cart))


# Q19. Store names of students present in class.
# Display Total Students, Search Student,
# Add Student and Remove Student.

students = ["Amit", "Sneha", "Rahul", "Priya"]

print("Total Students :", len(students))

name = input("Enter Student Name to Search : ")

if name in students:
    print("Student Present")
else:
    print("Student Not Present")

students.append("Riya")
students.remove("Rahul")

print("Updated Student List :", students)


# Q20. Create a list of books.
# Add, Search, Remove, Display and Count books.

books = ["Python", "Java", "C", "C++"]

books.append("HTML")

book = input("Enter Book Name to Search : ")

if book in books:
    print("Book Found")
else:
    print("Book Not Found")

books.remove("C")

print("Books List :", books)
print("Total Books :", len(books))

# Q21. Accept two lists and merge them into a single list.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

merged = list1 + list2

print("Merged List:", merged)


# Q22. Find common elements between two lists.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements:", common)

# Q23. Count the frequency of each element in a list.

numbers = [10, 20, 10, 30, 20, 10, 40]

visited = []

for i in numbers:
    if i not in visited:
        count = 0
        for j in numbers:
            if i == j:
                count += 1
        print(i, "occurs", count, "times")
        visited.append(i)

# Q24. Rotate a list:
# Left by one position and Right by one position.

numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + [numbers[0]]
right = [numbers[-1]] + numbers[:-1]

print("Original List:", numbers)
print("Left Rotation:", left)
print("Right Rotation:", right)


# Q25. Remove all duplicate elements while preserving order.

numbers = [10, 20, 30, 20, 40, 10, 50, 30]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List without Duplicates:", unique)


# Q26. Store marks of 20 students and determine:
# Highest, Lowest, Average, Above Average, Below Average.

marks = []

for i in range(20):
    mark = int(input("Enter Marks: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)


# Q27. Store salaries of employees and determine:
# Highest, Lowest, Average,
# Employees above ₹50000 and below ₹30000.

salary = []

n = int(input("Enter Number of Employees: "))

for i in range(n):
    s = int(input("Enter Salary: "))
    salary.append(s)

highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)

above50 = 0
below30 = 0

for i in salary:
    if i > 50000:
        above50 += 1
    if i < 30000:
        below30 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above 50000:", above50)
print("Employees Below 30000:", below30)


# Q28. Store scores of a batsman in 10 matches.
# Find Highest, Lowest, Total, Average,
# Centuries and Half-centuries.

scores = []

for i in range(10):
    score = int(input("Enter Score: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
half = 0

for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half-centuries:", half)





