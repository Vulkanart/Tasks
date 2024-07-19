#Отработка 3 Сортировка массива
n=8
A=[0, 1, 9, 2, 4, 3, 6, 5]
for i in range(n):
    imax=i
    for j in range (i+1, n):
        if A[j]>A[imax]: imax=j
    A[i], A[imax]=A[imax], A[i]
    print('A[', i, ']=', A[i])
