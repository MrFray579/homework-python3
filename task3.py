import math
list_1 = [1.1, 1.2, 3.1, 5, 10.01]
list_2 = list()
for i in range(len(list_1)):
    list_2.append(round(list_1[i] % 1, 2)) 
print(list_2)
result = max(list_2) - min(list_2)
print(result)
