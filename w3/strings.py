print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])# "e"

for x in "banana":
  print(x)
#b
#a
#n
#a
#n
#a

a = "Hello, World!"
print(len(a))#13

txt = "The best things in life are free!"
print("free" in txt)#True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

b = "Hello, World!"
print(b[2:5])#llo

b = "Hello, World!"
print(b[:5])#Hello

b = "Hello, World!"
print(b[-5:-2])#orl

a = "Hello, World!"
print(a.upper())#HELLO, WORLD!

a = "Hello, World!"
print(a.lower())#hello, world!
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))#Jello, World!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + " " + b
print(c) # returns "Hello World"

age = 36
txt = "My name is John, I am " + age
print(txt)# Error

age = 36
txt = f"My name is John, I am {age}"
print(txt) # My name is John, I am 36

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)# The price is 59.00 dollars

txt = "We are the so-called \"Vikings\" from the north."
print(txt) #We are the so-called "Vikings" from the north.

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""
