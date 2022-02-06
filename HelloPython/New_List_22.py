# Найти сумму чисел списка стоящих на нечетной позиции
a = [1,1,1,4,1,0]
Sum_of_odd = 0
for i in range(len(a)):
    if i % 2 != 0:
        Sum_of_odd = Sum_of_odd + a[i]
print(Sum_of_odd)