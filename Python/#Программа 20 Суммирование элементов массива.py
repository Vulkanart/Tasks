#Программа 20 Суммирование элементов массива
N=10
A=[0]*N
from random import randint
for i in range(N):
    A[i]=randint(50, 200)
for i in range(N):
    print('A[', i, ']=', A[i])
s=0
for i in range(N):
    s+=A[i]
print('s=', s)
