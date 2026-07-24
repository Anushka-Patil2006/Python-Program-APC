print("Hello, World!")
g="saylu"
a=("saii","Sayali","Harshee")
print(a)
b=["saii","sayali"]
print(b)
c={"name":"Sayali","age":"20"}
print(c)
d=8.90
print(d)
e=4+3j
print(e)
s=None
print(s)
val=True
print(val)


# Now we will see datatype of each var
print(type(g))
print(type(a))
print(type(b))
print("Type of variable c is:",type(c))
print(f"type of c:",type(c))
print(type(d))
print(type(e))
print("Type of s:",type(s))
print(type(val))

x=bytearray(5)
print(x)
print(type(x))
print("bytes datatype")
y=bytes(6)
print(y)
print(type(y))
print("MemoryView")
y=memoryview(b'\x00\x00\x00\x00\x00\x00')
print(y)
y2=memoryview(bytes(5))
print(y2)

print("range function")
n=range(10)
print(n)
print("Set")
z={"Apple","Banana","Cherry"}
print(z)
print(type(z))

print("FrozenSet Datatype")
q=frozenset({"Apple","Banana"})
print(q)
print(type(q))
print("************")

print("Arithemetic Operators")
x2=4
x3=5
print(x2)
print(x2+x3)
z=4+5
print(z)
print("Addition is:",x2+x3)
print("subtraction is:",x2-x3)
print("Product is:",x2*x3)
print("division is:",x2/x3)
print("Modulus is:",x2%x3)
print("Exponential is:",x2**x3)
print("Floor Division:",x2//x3)
print("************")

print("Assignment Operators")
m=3
print(m)
m+=3 #m=m+3
print("Addition:",m)
m-=2 #m=m-2
print("Subraction:",m)
m*=4 #m=m*4
print("product is:",m)
m/=2 #m=m/2
print("division is:",m)
m%=100 #m=m%100
print("Mod is:",m)
m//=2 #m=m//2
print("floor div:",m)
m**=2 #m=m**2
print("Exponential is:",m)
print("*********")

print("Comparison Operator")
a2=6
a3=8
print("a2 is small :",a2>a3)
print("a3 is big:",a2<a3)
print("a2 is less than or equal to:",a2<=a3)
print("a3 is grater than or equal to:",a2>=a3)
print("both are Equal or not:",a2==a3)
print("both are not equal:",a2!=a3)
print("*************")

print("Logical Operators")
#just trial
b2=9
b3=8
print(b2 or b3)
print(b3 or b2)

print("Actual thinking")
f=90
print(f<4 or f<105) #if any one codition becomes true then op will be 1 means true
print(f<105 and f<4) #if both condition becomes true then and then op will be 1 means true
w=False #it reverses output 
print(not w)
print("******************")
print("Identity Operator")
x=7
y=8
print(x is y)
print(y is x)
print(x is not y)
print(y is not x)
print("Equality concept comes here")  #these operators are useful for checking or comapring the equality

h=4
e=4
print(h is e)  #is operator for surity that values are equal
print(e is h)
print(h is not e) #is not operator means values are diffrent
print(e is not h)
print("********************")

print("Membership Operator")
listt=["lily","Sunflower","Rose","Marigold"]
print("sunflower" in listt)   #in operator checks the obj is available in listt or not
print("Sunflower" in listt)
print("--------")
print("Almond" in listt)
print("Almond" not in listt) #not in operator means given obj is notin listt

print("BitWise Operators")
x=3
print(x<<3)
print(x>>3)
print(~x)

print("Using Seperator")
print("04","11","2005",sep="-")
print("Sayali",end=" @Deshmane")
print("\n")

#Using % operator
q1=23
print("The hexadecimal %x"%q1)
print("the octal value is %o"%q1)
stringg="Hello World"
print("The String value is %s"%stringg)
f=9.8
print("The float value is %f"%f)
print("##################")

#let me ask can we print all these into one sentence
print("The hexadecimal %x\nThe octal value is %o\nThe String value is %s\nThe float value is %f" % (q1, q1, stringg, f))