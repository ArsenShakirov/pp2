def trapezoid_area(h,a,b):
  return (a+b)*h/2
h = int(input("Height "))
a = int(input("Base first "))
b = int(input("Base Second "))
area = float(trapezoid_area(h,a,b))
print("Expected Output: ", round(area, 1))
