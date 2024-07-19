#Задание 1.5 29 Среднее арифметическое 10 случайных чисел
a=0
from random import randint
for i in range (10):
    x=randint(1, 20)
    print('{:3d}'.format(x), end='')
    a=a+x
print(' Среднее арифметическое =', a/10)
