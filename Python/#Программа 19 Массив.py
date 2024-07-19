#Программа 19 Массив
N=10
A=[0]*N
from random import randint
for i in range(N):
    A[i]=randint(0,99)
for i in range(N):
    print('A[', i, ']= ', A[i])
