# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import randint, random

list_S = [round(randint(1, 9) + random(), 2) for i in range(randint(3, 10))]
print(list_S)

def f(list_work):
    list_d = []
    for i in range(len(list_work)):
        list_d.append(round(list_work[i] - int(list_work[i]), 2))

    return max(list_d) - min(list_d)

print(f(list_S))
