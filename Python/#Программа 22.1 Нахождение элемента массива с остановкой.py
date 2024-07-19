#Программа 22.1 Нахождение элемента массива с остановкой
N=10
A=[0]*N
from random import randint
for i in range(N):
    A[i]=randint(0, 99)
    print('A[', i, ']=', A[i])
x=int(input('x='))
nx=-1
for i in range(N):
    if A[i]==x:
        nx=i
        break
if nx>=0:
    print('A[{}]={}'.format(nx, x))
else:
    print('Элемент не найден.')
