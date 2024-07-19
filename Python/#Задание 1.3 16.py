#Задание 1.3 16
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
l=(a+b+c)/2
from math import *
S=sqrt(l*(l-a)*(l-b)*(l-c))
print('S =', S)
