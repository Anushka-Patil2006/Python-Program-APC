
#1. Write a Python program to create a tuple of five integers and display it.
t=(10,20,30,40,50)
print(t)

#2.Create a tuple containing five city names. Display:First city,  Last city ,Third city
t=("Satara","Karad","Pune","Mumbai","Kolhapur")
print(t[0])
print(t[4])
print(t[2])

#3.Create a tuple of student names and display the total number of students using the len() function.
t=("Anushkaa","Janhavi","Snehal","Tanaya","Amruta")
print("Total number of student: ",len(t))

#4.Create a tuple of colors. Check whether a given color exists in the tuple
t=("Blue","Green","Pink","Purple","White")
color=input("Enter Color: ")
flag=0
for i in t:
    if i==color:
        flag=1
        break
    
if flag==1:   
    print("Present in Tuple")
else:
    print("Not present in tuple")

#5.Create a tuple of fruits and display each fruit using a loop.
t=("Mango","Watermelon","Cherry","Banana")
for i in t:
    print(i)

#6.Create a tuple with repeated numbers and count how many times a particular number appears.
t=(1,2,3,4,5,1,2,2,3)
print(t.count(2))

#7.Create a tuple of employee IDs and find the index of a given ID.
t=(101,102,103,104,105)
print(t.index(104))

#8.Create two tuples of numbers and concatenate them into a single tuple.
t1=(1,2,3,4)
t2=(5,6,7,8)
print(t1+t2)

#9.Create a tuple containing three elements and repeat it four times.
t=(1,2,3)
print(t*4)

#10.Create a tuple of 10 numbers and display: First five elements, Last five elements, Middle four elements,Alternate elements,Reverse tuple
t=(10,20,30,40,50,60,70,80,90,100)
print("1st five element :",t[0:5])
print("Last five element:",t[10:5])
print("Middle Four Element: ",t[3:8])
print("Alternate Element:",t[0::2])
print("Reverse Element:",t[::-1])

#11.Convert a tuple into a list and add a new element.
t=(10,20,30)
ls=list(t)
print("List from tuple:",ls.append(40))



# 12. Accept five numbers from the user, store them in a list,
#    and convert the list into a tuple.

numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

t = tuple(numbers)

print("Tuple:", t)


# 13. Modify a tuple by converting it into a list and then
#    back into a tuple.

t = (10, 20, 30, 40)

l = list(t)
l[1] = 50

t = tuple(l)

print("Modified tuple:", t)


# 14. Create a tuple and delete it completely.

t = (10, 20, 30, 40)

del t

print("Tuple deleted successfully.")


# 15. Create a nested tuple containing student details and
#    display each record.

students = (
    (1, "Anu", "Computer", 85),
    (2, "Rahul", "IT", 78),
    (3, "Sneha", "Computer", 92)
)

for student in students:
    print(student)


# 16. Store ten numbers in a tuple and calculate their sum.

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = 0

for n in numbers:
    total = total + n

print("Sum:", total)


# 17. Find the largest and smallest number in a tuple without
#    using max() and min().

numbers = (45, 12, 78, 34, 90, 23, 56)

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)


# 18. Calculate the average of elements stored in a tuple.

numbers = (10, 20, 30, 40, 50)

total = 0

for n in numbers:
    total = total + n

average = total / len(numbers)

print("Average:", average)


# 19. Store 15 integers in a tuple and count even and odd
#    numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 10. Accept a number from the user and determine whether it
#     exists in the tuple.

numbers = (10, 20, 30, 40, 50)

n = int(input("Enter number to search: "))

if n in numbers:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")


# 21. Store student details in a tuple and display all details.

student = (101, "Anushka", "Computer Engineering", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


# 22. Create tuples containing Employee ID, Name and Salary.
#     Display all employee information.

employees = (
    (101, "Rahul", 30000),
    (102, "Sneha", 35000),
    (103, "Amit", 40000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print("--------------------")


# 23. Store item prices in a tuple and calculate total bill,
#     average price, highest price and lowest price.

prices = (100, 250, 150, 300, 200)

total = 0

for price in prices:
    total = total + price

average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)


# 24. Store temperatures of seven days and determine maximum,
#     minimum and average temperature.

temperatures = (32, 35, 31, 30, 36, 34, 33)

total = 0
maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    total = total + temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)


# 25. Store runs scored in 10 matches and calculate total runs,
#     highest score, lowest score and average score.

runs = (45, 78, 32, 90, 56, 67, 12, 88, 54, 70)

total = 0
highest = runs[0]
lowest = runs[0]

for run in runs:
    total = total + run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)


# 26. Create two tuples and find the common elements between
#     them.

t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = []

for n in t1:
    if n in t2:
        common.append(n)

print("Common elements:", tuple(common))


# 27. Merge two tuples and remove duplicate elements.

t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

merged = t1 + t2

unique = []

for n in merged:
    if n not in unique:
        unique.append(n)

result = tuple(unique)

print("Merged tuple without duplicates:", result)


# 28. Count the frequency of each element in a tuple.

numbers = (10, 20, 10, 30, 20, 10, 40, 30)

counted = []

for n in numbers:
    if n not in counted:
        count = 0

        for x in numbers:
            if x == n:
                count = count + 1

        print(n, "occurs", count, "times")
        counted.append(n)


# 29. Convert a tuple into a sorted tuple in ascending and
#     descending order.

numbers = (50, 20, 80, 10, 40, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)


# 30. Create a tuple containing patient records.
#     Display records, search by ID, count patients and display
#     patients with a specific blood group.

patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Amit", 40, "O+"),
    (104, "Priya", 28, "A+"),
    (105, "Rohan", 35, "B+")
)

# Display all patient records
print("All Patient Records:")

for patient in patients:
    print(patient)


# Search for a patient by ID
search_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("Patient Found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if found == False:
    print("Patient not found.")


# Count total number of patients
print("Total number of patients:", len(patients))


# Display patients with a specific blood group
blood_group = input("\nEnter blood group to search: ")

print("Patients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)

















