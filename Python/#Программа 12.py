#Программа 12
print('Решение линейного уравнения')
a=float(input('Введите коэффициент а>>'))
b=float(input('Введите коэффициент b>>'))
if a!=0:
    x=-b/a
    print('Корень уравнения x=', x)
elif b!=0:
    print('Корней нет')
else:
    print('x - любое число')
