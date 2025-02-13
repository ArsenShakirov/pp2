import math

def polygon_area(n, a):
    return (n * a ** 2) / (4 * math.tan(math.pi / n))

n = int(input("number of sides: "))
a = float(input("length of side: "))

area = polygon_area(n, a)

print("The area of the polygon is:", round(area, 0))
