#Программа15 Через сколько спортсмен будет бегать 25 км.
print('График тренировок')
i=1; x=10
while True:
    i+=1
    x=x+0.1*x
    if x>=25: break
print('Начиная с ', i, '-го дня спортсмен будет пробегать 25 км', sep='')
