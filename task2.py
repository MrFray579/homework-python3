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

# 2 вариант
list_1 = [3, 2, 4, 5, 6]
len_list = 0
if len(list_1) % 2 == 0:
    len_list - len(list_1)//2
else:
    len_list = len(list_1)//2 + 1

for i in range (len_list):
    print(list_1[i] * list_1[len(list_1)-1-i])
