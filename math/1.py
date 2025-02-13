import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("degree: "))
radian = degree_to_radian(degree)

print("radian:", round(radian, 6))
d
