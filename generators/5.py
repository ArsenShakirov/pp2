def even_numbers(n):
    for i in range(0, n + 1):
        yield str(i)

n = int(input("Enter a number: "))
mylist = list(even_numbers(n))
mylist.sort(reverse=True)
print(" ".join(mylist))
