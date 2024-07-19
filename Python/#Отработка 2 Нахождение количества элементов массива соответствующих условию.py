#Отработка 2 Нахождение суммы значений элементов массива соответствующих условию
N=10
A=[0]*10
from random import randint
for i in range (0, N):
    A[i]=randint(0, 99)
    print('A[', i, ']=', A[i])
s=0
for i in range(10):
    if A[i]>50 and A[i]<60: s+=A[i]
print('s=', s)
