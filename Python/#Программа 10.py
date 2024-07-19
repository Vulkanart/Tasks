#Программа 10
print('Нахождение наибольшей из трёх величин')
a=int(input('Введите а:'))
b=int(input('Введите b:'))
c=int(input('Введите c:'))
y=a
if b<y:
    y=b
if c<y:
    y=c
print('y=', y)
