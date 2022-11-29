#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
import random

n = random.randint(1, random.randint(10, 20))
list_feb = [0, 1]
for i in range(n - 1):
    list_feb.append(list_feb[-2] + list_feb[-1])

list_negafib = []
for num, i in enumerate(list_feb[1:]):
    print(i)
    if num % 2 == 0:
        list_negafib.append(i)
    else:
        list_negafib.append(i * (-1))

resault_list = [i for i in list_negafib[::-1] + list_feb]


print(resault_list)


