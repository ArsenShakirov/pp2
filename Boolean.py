print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  #b is not greater than a

print(bool("Hello"))  #True
print(bool(15))       #True

x = "Hello"
y = 15

print(bool(x))  #True
print(bool(y))

bool("abc")  #True
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)  #False
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))  #False

def myFunction() :
  return True

print(myFunction())  #True

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")  #YES!

x = 200
print(isinstance(x, int))  #True
