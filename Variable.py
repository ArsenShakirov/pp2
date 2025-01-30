x = 5
y = "John"
print(x)  #5
print(y)  #John

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    #Sally

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))  #<class 'int'>
print(type(y))  #<class 'str'>

x = "John"
# is the same as
x = 'John'

a = 4         #4 if print(a)
A = "Sally"   #Sally if print(A)
#A will not overwrite a

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

x, y, z = "Orange", "Banana", "Cherry"
print(x)  #Orange
print(y)  #Banana
print(z)  #Cherry

x = y = z = "Orange"
print(x)  #Orange
print(y)  #Orange
print(z)  #Orange

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  #apple
print(y)  #banana
print(z)  #cherry

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  #all output: Python is awesome

x = 5
y = 10
print(x + y)  #15

x = 5
y = "John"
print(x, y) #5 John

#GLobal variable

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()  #Python is awesome

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()  #Pyhton is fantastic

print("Python is " + x)  #Pyton is awesome

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic
