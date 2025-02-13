def square_generator(N):
    for i in range(N + 1):
        yield i * i

N = 10
for square in square_generator(N):
    print(square)
