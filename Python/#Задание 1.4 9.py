#Задание 1.4 9
x=int(input('Введите трёхзначное число>>'))
a=x//100
b=x%100//10
c=x%10
if a==c:
    print('Перевёртыш')
else: print ('Нет')
