# 1.To check whether no is zero or not.

num=int(input("Enter Number: "))
if num==0:
    print("Given number is zero")
else:
    print("Given number is non zero")


# 2.Largest no among two nos

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1>n2:
    print(n1," is greater than", n2)
else:
    print(n2," is greater than", n1)


# 3.Positive or negative number

no=int(input("Enter number: "))
if no>0:
    print(no,"is Positive Number")
else:
    print(no,"is Negative Number")


# 4.Vowel or consonent

v1=input("Enter alphabet: ")
if v1=='a'or v1=='e'or v1=='i'or v1=='o'or v1=='u':
    print("Vowel")
else:
    print("Consonent")  


# 5. Student Mark

m1=int(input("Enter student mark:"))
if m1>=90:
    print("Excellent Performance")
elif m1>=80:
    print("Very Good")
elif m1>=70:
    print("Good")
elif m1>=60:
    print("Average Performance")
else:
    print("Poor")
print("--------------------------------------------------------") 


# 6. Smallest number among 3 nos
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
if n1<n2 and n1<n3:
    print(n1,"is smallest number")
elif n2<n1 and n2<n3:
    print(n2,"is smallest number")
else:
    print(n3,"is smallest number")
print("--------------------------------------------------------") 

# 7. Leap Year

year=int(input("Enter Year: "))
if year%400==0:
    print(year," is Leap Year")
else:
    if year%4==0:
        print(year," is Leap Year")
    else:
        print(year, "is not Leap Year")
print("--------------------------------------------------------") 

# 8. Even or Odd

n=int(input("Enter number: "))
if n%2==0:
    print(n,"is Even Number")
else:
    print(n,"is Odd Number")
print("--------------------------------------------------------") 

# 9.Gender check

status=input("Enter Marriage Status: ")
gen=input("Enter gender: ")
age=int(input("Enter age: "))

if status=="married":
    print("Driver Insured")
elif status=="unmarried" and age>=30 and gen=="male":
    print("Driver Insured")
elif status=="unmarried" and gen=="female" and age>=25:
    print("Driver Insured")
else:
    print("driver not insured")



# 1.wap to print the natural no upto n. read n from user

n=int(input("Enter value of n: "))
i=1
while i<=n:
    print(i)
    i=i+1
#2. wap to print even odd no upto n.numerator from user
n=int(input("Enter value of n: "))
i=1
while i<=n:
    if i%2==0:
        print("Even: ",i)
    else:
        print("Odd: ",i)
    i=i+1

#3 wap to print sum of natural no upto n

n=int(input("Enter value of n: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of Natural no: ",sum)

#4 wap to print sum of all no upto n

n=int(input("Enter value of n: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of Natural no: ",sum)

#5. wap print sum of even no upto n

n=int(input("Enter value of n: "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("Sum of Even no: ",sum)

#6. wap to print natural no upto n in reverse order

n=int(input("Enter value of n: "))
i=n
while i>=1:
    print(i)
    i=i+1

#7. wap to print fibonnacii serias upto n

n = int(input("Enter n: "))

a = 0
b = 1

while a <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#8. wap to check no is prime or not
n = int(input("Enter number: "))

i = 2
prime = True

if n <= 1:
    prime = False
else:
    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

if prime:
    print("Prime Number")
else:
    print("Not Prime Number")

#9. wap to find sum of digit of entered no

n = int(input("Enter number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum =", sum)

#10. wap to check entered no is palindrome or not

n = int(input("Enter number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#11. wap to print multiplication table.

n = int(input("Enter number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

#12. wap to print largest and smallest no from n numbers.

n = int(input("How many numbers? "))

i = 1

num = int(input("Enter number: "))
largest = num
smallest = num

while i < n:
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    i += 1

print("Largest =", largest)
print("Smallest =", smallest)



















