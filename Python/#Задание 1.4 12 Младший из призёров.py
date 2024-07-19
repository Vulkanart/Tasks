#Задание 1.4 12 Младший из призёров
a, b, c, d=map(int,input('Введите возраст 4х призёров через запятую^').split())
x=a
if b<x:
    x=b
if c<x:
    x=c
if d<x:
    x=d
print(x)
