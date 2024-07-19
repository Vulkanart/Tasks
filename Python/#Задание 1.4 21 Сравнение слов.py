#Задание 1.4 21 Сравнение слов
a=input('Введите 1е слово: ')
b=input('Введите 2е слово: ')
c=input('Введите 3е слово: ')
if len(a)==len(b)==len(c): print('Все слова одинаковые')
if len(a)>len(b)and len(a)>len(c): print('Самое большое 1е слово')
if len(b)>len(a)and len(b)>len(c): print('Самое большое 2е слово')
if len(c)>len(a)and len(c)>len(b): print('Самое большое 3е слово')

