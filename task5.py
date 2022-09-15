n = int(input('Введите число: '))
fib = 1
fib2 = -1
print(fib, fib2, end=' ')
for i in range(2, n):
    fib, fib2 = fib2, fib - fib2
    print(fib2, end=' ')

f1 = f2 = 1
print(0, f1, f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')








