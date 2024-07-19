#Задание 1.3 15
xa, ya=map(float,input('Введите координаты точки А>>').split())
xb, yb=map(float,input('Введите координаты точки B>>').split())
from math import *
d=sqrt(((xb-xa)**2)+((yb-ya)**2))
print('|AB| =', '{:5.1f}'.format(d))
