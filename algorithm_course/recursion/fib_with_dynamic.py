def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a


print(fib(50))