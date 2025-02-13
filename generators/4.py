def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("start number: "))
b = int(input("end number: "))

for square in squares(a, b):
    print(square)
