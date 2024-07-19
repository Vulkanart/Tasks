#Задание 1.4 6
print('Введите три числа: ')
x, y, z=map(int, input().split())
if x<=y<=z:
    x*=2
    y*=2
    z*=2
else:
    x-=2
    y-=2
    z-=2
print(x, y, z)
