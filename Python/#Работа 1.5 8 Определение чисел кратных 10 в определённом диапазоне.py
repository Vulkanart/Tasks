#Работа 1.5 8 Определение чисел кратных 10 в определённом диапазоне
print('Вваедите a и b в диапазоне: 1<a<b<30 000')
a=int(input())
b=int(input())
k=0
for i in range (a, b+1):
    if i%10==0:
        k+=1
print(k)
