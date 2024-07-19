#Задание 1.4 15 Обмен значений переменных
x=int(input('x>>'))
y=int(input('y>>'))
if x>y:
    x=x+y
    y=x-y
    x=x-y
    print('x=', x)
    print('y=', y)
else:
    print('x=', x)
    print('y=', y)
