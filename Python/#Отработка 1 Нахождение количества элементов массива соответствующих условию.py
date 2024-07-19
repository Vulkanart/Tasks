#Отработка 1 Нахождение количества элементов массива соответствующих условию
N=10
A=[0]*N
from random import randint
for i in range (0, N):
    A[i]=randint(0, 99)
    print('A[', i, ']=', A[i])
k=0
for i in range(10):
    if A[i]>50: k+=1
print('k=', k)
