#Задание 1.5 9.26 План отлова рыбы в пруду
A=float(input('Запас рыбы в пруду:'))
B=float(input('План отлова:'))
C=float(input('Наименьший запас:'))
L=0
while A>=C:
    A=(A+A*0.15)-B
    L=L+1
print('Заданный план можно выдерживать в количестве', L, 'лет.')
print('Остаток рыбы в пруду:', A)
