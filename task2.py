import math
n = int(input('Введите количество чисел: '))
arr = list()
for i in range(n):
    arr.append(int(input('Введите числа: ')))
print(arr)
arr2 = list()
for i in range(math.ceil(len(arr)/2 )):
    arr2.append(arr[i] + arr[-i-1])
print(arr2)
