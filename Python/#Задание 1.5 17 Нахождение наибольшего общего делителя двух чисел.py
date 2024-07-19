#Задание 1.5 17 Нахождение наибольшего общего делителя двух чисел
a,b=map(int,input('Введите два числа>>').split())
while a!=b:
    if a>b: a=a-b
    else: b=b-a
print(a)
