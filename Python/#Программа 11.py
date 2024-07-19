#Программа 11
from math import *
print('Решение квадратного уравнения')
print('Введите коэффициенты a, b, c>>')
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
d=b*b-4*a*c
if d<0:
    print('Корней нет')
if d==0:
    print('Корень уравнения x=', '{:6.4f}'.format(x))
if d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print('Корни уравнения:')
    print('x1=', '{:6.4f}'.format(x1))
    print('x2=', '{:6.4f}'.format(x2))
