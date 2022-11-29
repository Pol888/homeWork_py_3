# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import random

X = random.randint(1, 100)
print('Число Х = ', X)

resault = ''

while X != 0:
    resault += str(X % 2)
    X //= 2
resault = resault[::-1]

print(resault)