#Задание 1.4 20 Дополнить число до ста
from random import randint
a=randint(0, 100)
print(a)
x=int(input('Введите число, чтобы в сумме получилось 100>>'))
print(a, '+', x, '=', a+x)
if a+x==100:
    print('Верно')
else: print('Не верно')
