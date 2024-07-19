#Задание 1.3 10
from random import randint
x=randint(10, 99)
a=x//10
b=x%10
print('Число', (x))
print('Сумма цифр числа = ', a+b)
print('Произведение цифр числа = ', a*b)
print('Перестановка цифр числа = ', b, a, sep='')
