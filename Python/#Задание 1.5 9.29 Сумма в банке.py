#Задание 1.5 9.29 Сумма в банке
a=10000
b=a*2
c=0
while a<=b:
    a=a+a*0.05
    c+=1
print(c, b, a, sep='\n')
