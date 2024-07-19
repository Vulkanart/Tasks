#Задание 1.5 7 Факториал числа
n=int(input('Введите n>>'))
k=1
f=1
while k<=n:
    f=f*k
    k+=1
print(f"{n}! = {f}")
