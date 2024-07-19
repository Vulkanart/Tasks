#Программа 21 Нахождение наибольшего элемента массива
N=10
A=[0]*N
from random import randint
for i in range(N):
    A[i]=randint(0, 99)
    print('A[', i, ']=', A[i])
imax=0
for i in range (1, N):
    if A[i]>A[imax]: imax=i
print('Наибольший элемент: ', A[imax])
