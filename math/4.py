def paralelo_area(h,a):
  return a*h

h = int(input("Height: "))
a = int(input("Base: "))

area = float(paralelo_area(h,a))
print("Expected Output: ", round(area, 1))
