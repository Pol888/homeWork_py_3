# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

from random import randint

list_S = [randint(1, 9) for i in range(randint(3, 10))]
list_P = []
if len(list_S) % 2 != 0:
    for i in range(0, len(list_S) // 2 + 1):
        list_P.append(list_S[i] * list_S[-(i + 1)])
else:
    for i in range(0, len(list_S) // 2):
        list_P.append(list_S[i] * list_S[-(i + 1)])

print('Лист-', list_S)
print('Лист произведений-', list_P)