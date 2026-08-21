#1.Write a Python program to create a set containing five integers and display all its elements.
s="Hello"
print(s.isnumeric())
print(s.islower())
print(s.istitle())




s={10,20,30,40,50}
print(s)

#2.Create a list containing duplicate values. Convert the list into a set and display the resulting set.
l1=[10,20,10,30,20,40,10,50]
s=set(l1)
print(s)

#3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
s={"Apple","Cherry","Grapes","Mango"}
s.add("Mango")
s.add("Watermelon")
print("Updated Set:",s)

#4.Create a set of numbers and remove a specified number from the set.
s={10,20,30,40,50,60}
s.remove(60)
print("After removing:",s)

#5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
s={"Shreya","Sonali","Jui","Snehal","Tanaya","Janhavi"}
nm=input("Enter Any Student Name:")
for i in s:
    if i==nm:
        print("Student Present")
        

#6.Create a set of cities and determine the total number of cities using an appropriate function.
s={"Karad","Patan","Satara","Pune","Mumbai","Baramati"}
print("Total Number Of Cities:",len(s))

#7.Create a set of programming languages and display each language using a for loop.
s={"C","C++","Java","Javascript","SQL","PHP","Python"}
for i in s:
    print(i)

#8.Create a list containing duplicate numbers, use a set to remove the duplicates.
l=(10,20,10,30,20,10,40,10,50,40)
s=set(l)
print(s)

#9.Create two sets of integers and find their union.
s1={10,20,30,40}
s2={30,40,50,60}
print("Union of Set:",s1.union(s2))

#10.Create two sets and find the elements common to both sets.
s1={10,20,30,40}
s2={30,40,50,60}
print("Common Element in set:",s1.intersection(s2))
print("Difference:",s1.difference(s2))
print("Symmentric Difference:",s1.symmetric_difference(s2))

#11.Create two sets and find:
#•Elements present in the first set but not the second 
#•Elements present in the second set but not the first
s1={10,20,30,40}
s2={30,40,50,60}
print("Present in set 1:",s1.difference(s2))
print("Present in set 2:",s2.difference(s1))

#12. Create two sets of numbers and find the elements that are present in either set but not in both.
s1={10,20,30,40}
s2={30,40,50,60}
print("Element present in either one set",s1.symmetric_difference(s2))

#13. Create two sets and determine whether the first set is a subset of the second set.
s1={10,20,30,40}
s2={30,40,50,60}
print("Subset of second set:",s1.issubset(s2))

#14. Create two sets and determine whether the first set is a superset of the second set.
s1={10,20,30,40}
s2={30,40,50,60}
print("Subset of second set:",s1.superset(s2))

#15. Write a program to determine whether two sets have no elements in common.
s1={10,20,30,40}
s2={30,40,50,60}
print("Element present in either one set",s1.symmetric_difference(s2))

#16. Create two sets and check whether they are equal.
s1={10,20,30,40}
s2={30,40,50,60}
if s1==s2:
    print("Sets are equal")
else:
    print("Sets not equal")

#17. Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
s1={"Math","Marathi","English","Hindi","Sanskrit"}
s2={"Science","Hindi","Sanskrit"}
print("Subject studied by both:",s1.intersection(s2))

# 18. Display all unique words from a sentence using a set

sentence = input("Enter a sentence: ")
words = set(sentence.lower().split())

print("Unique words:", words)


# 19. Students present in morning and afternoon sessions

morning = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
afternoon = {"Rahul", "Priya", "Rohan", "Neha", "Kiran"}

print("Present in both sessions:", morning & afternoon)
print("Only in morning:", morning - afternoon)
print("Only in afternoon:", afternoon - morning)
print("Present in at least one session:", morning | afternoon)


# 20 & 21. Students enrolled in Python and Java

python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Rahul", "Priya", "Rohan", "Kiran"}

print("Students in both courses:", python_students & java_students)
print("Students in only one course:",
      python_students ^ java_students)


# 22. Technical skills of two employees

employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

print("Common skills:", employee1 & employee2)
print("Skills unique to Employee 1:", employee1 - employee2)
print("Skills unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)


# 23. Available books and requested books

available_books = {"Python Basics", "Java Programming", "Data Science", "DBMS"}
requested_books = {"Python Basics", "DBMS", "Machine Learning", "Java Programming"}

print("Requested books that are available:",
      available_books & requested_books)


# 24. Visitor IDs from two different days

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Visitors only on first day:", day1 - day2)
print("Visitors only on second day:", day2 - day1)


# Products belonging to different categories

category1 = {"Laptop", "Mobile", "Tablet", "Smartwatch"}
category2 = {"Mobile", "Tablet", "Camera", "Headphones"}

print("Products belonging to both categories:",
      category1 & category2)


# 25. Friends of two users

user1 = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
user2 = {"Rahul", "Priya", "Rohan", "Kiran", "Neha"}

print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)











