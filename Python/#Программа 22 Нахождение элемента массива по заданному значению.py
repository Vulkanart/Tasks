#Программа 22 Нахождение элемента массива по заданному значению
N=10
A=[0]*N
from random import randint
for i in range(N):
    A[i]=randint(0, 99)
    print('A[', i, ']=', A[i])
x=int(input('x='))
nx=-1
for i in range (0, N):
    if A[i]==x: nx=i
if nx==-1:
    print('Элемента со значением, равным', x, 'нет.')
else:
    print('Индекс элемента, равного заданному,', nx)
