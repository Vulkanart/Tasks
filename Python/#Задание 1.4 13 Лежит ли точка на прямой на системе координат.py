#Задание 1.4 13 Лежит ли точка на прямой на системе координат
k, m=map(int,input('k, m>>').split())
xa, ya=map(int,input('xa, ya>>').split())
y=k*xa+m
if ya>y: print('Точка лежит над прямой')
if ya==y: print('Точка лежит на прямой')
if ya<y: print('Точка лежит под прямой')
