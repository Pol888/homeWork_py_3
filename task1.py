# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

from random import randint


list_S = [randint(1, 9) for i in range(10) ]

sum_S = 0
for i in range(1, len(list_S), 2):
    sum_S += list_S[i]

print(list_S)
print(sum_S)
