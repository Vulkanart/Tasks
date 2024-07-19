#Задание 1.4 11
a, b, c=map(int,input('a b c >>').split())
if a<b+c and b<a+c and c<a+b:
    if (a==b and a!=c and b!=c) or (b==c and b!=a and c!=a) or (c==a and c!=b and a!=b):
        print('Равнобедренный')
    if a==b==c:
        print('Равносторонний')
    if a!=b!=c:
        print('Разносторонний')
else:
    print('Не сушествует')
