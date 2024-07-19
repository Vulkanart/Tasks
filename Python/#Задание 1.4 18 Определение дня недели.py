#Задание 1.4 18 Определение дня недели
chislo=int(input('Chislo>>'))
if chislo%7==3: print('Понедельник')
if chislo%7==4: print('Вторник')
if chislo%7==5: print('Среда')
if chislo%7==6: print('Четверг')
if chislo%7==0: print('Пятница')
if chislo%7==1: print('Суббота')
if chislo%7==2: print('Воскресенье')
