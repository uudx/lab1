x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

n = str(3)    # n will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

a,b,c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

fruits = ["apple", "banana", "cherry"]
q, w, e = fruits
print(q)
print(w)
print(e)

print(q, w, e)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
