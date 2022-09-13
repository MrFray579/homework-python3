n = int(input('Введите количество чисел: '))
arr = list()
for i in range(n):
    arr.append(int(input('Введите числа: ')))
print(arr)
result = 0
for i in range(1, len(arr), 2):
    result += arr[i]
print(f'Сумма элементов на нечетных позициях = {result}')