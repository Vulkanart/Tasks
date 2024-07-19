#Задание 1.5 28 Вычисление первых n чисел
n=int(input('Введите число>>'))
a, b, c, d=0, 0, 0, 0
for i in range(1, n+1):
    a=a+i
    b=b+i**2
    if i%2==0: c=c+i
    if i>9 and i<100: d=d+i
print(a, b, c, d)
