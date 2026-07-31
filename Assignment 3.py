#1. Write a PYTHON program to print the natural numbers up to n

n=int(input("Enter value of n: "))
for i in range(1,n+1):
      print(i)


# 2.Write a PYTHON program to print even numbers up to n

n=int(input("Enter value of n: "))
for i in range(1,n+1):
    if i%2==0:
        print(i) 

# 3.Write a PYTHON program to print odd numbers up to n

n=int(input("Enter value of n: "))
for i in range(1,n+1):
    if i%2!=0:
        print(i) 

# 4.Write a PYTHON program that prints  1 2 4 8 16 32 … n2

n=int(input("Enter value of n: "))
j=1
for i in range(1,n+1):
    print(j)
    j=j*2   

# 5.Write a PYTHON program to sum the given sequence
#     1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!

n=int(input("Enter value of n: "))
fact=1
total=1
for i in range(1,n+1):
    fact=fact+i
    total=total+(1/fact)

print("Sum is: ",total)

# 6. Write a PYTHON program to compute the cosine series
#          cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!


# 7.Write a short PYTHON program to check weather the square root of number is prime or  not.

import math
n=int(input("Enter number: "))
root = int(math.sqrt(n))
#root=(n**0.5)
flag=False
for i in range(2,n):
    if root%i==0:
        flag=True
        break

if flag==True:
    print("Square root of given number is not prime")
else:
    print("Square root of given number is  prime") 

# 8.Write a PYTHON program to produce following design
#			A B C 
#			A B C 
#			A B C

for i in range(3):
    for j in range(65,68):  #65 and 68 are the ascii code 
        print(chr(j), end=" ")
    print()  

# 9. Write a PYTHON program to produce following design
#      A
#      A B
#      A B C
#      A B C D 
#      A B C D E
#      If user enters n value as 5

n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()  

# 10. Write a PYTHON program to produce following design
#      A B C D E
#      A B C D
#      A B C
#      A B
#      A                           (If user enters n value as 5)

n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    for j in range(65,65+n-i):
        print(chr(j), end=" ")
    print()    

#11. Write a PYTHON program to produce following  
#     design
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
#     If user enters n value as 5

n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 

# 12. Write a PYTHON program to produce following design
#     1
#     2 2
#     3 3 3
#     4 4 4 4 
#     5 5 5 5 5
#     If user enters n value as 5

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()    


#---------------------------------------------------------
#---------------------------------------------------------
#string problem

# 1.String Length 

s=input("Enter string: ")
length=0
for i in s:
    length=length+1

print("Length of String: ",length) 

#2.Character Count

s = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in s:
    if ch in "AEIOUaeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)
# Reverse a string

s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

print("Reversed string:", rev)

# Check whether a string is palindrome

s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Count uppercase and lowercase letters

s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)


# Replace one character with another

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("New string:", result)

# Remove spaces from a string

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("String without spaces:", result)

# Count frequency of a character

s = input("Enter a string: ")
ch = input("Enter the character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency =", count)

# Program to print first and last character

s = input("Enter a string: ")

print("First character =", s[0])
print("Last character =", s[-1])

# Program to display ASCII value of each character

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))

# Program to count words in a sentence

s = input("Enter a sentence: ")

words = s.split()

print("Total words =", len(words))

# Program to find the longest word

s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)

# Program to find the shortest word

s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word =", shortest)



