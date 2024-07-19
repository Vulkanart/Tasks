#Задание 1.4 10
x1, y1=map(int,input('Координаты 1-й точки>>').split())
x2, y2=map(int,input('Координаты 2-й точки>>').split())
from math import *
A=sqrt(x1**2+y1**2)
B=sqrt(x2**2+y2**2)
if A>B:
    print('2-я точка ближе')
elif A<B:
    print('1-я точка ближе')
else: print('Точки равноудалены')
