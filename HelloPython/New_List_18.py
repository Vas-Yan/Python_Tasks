# Реализовать алгоритм перемешивания списка
# from random import *
# from types import new_class # * позволяет импортировать все функции
# new_array = [i for i in range(10)]
# def random_sorting(a):
#     for i in range(len(a)-1):
#         number = a[i] 
#         index = randint(i+1,len(a)-1)
#         a[i] = a[index]
#         a[index] = number
#     return a
# print(new_array)
# print(random_sorting(new_array))

# упрощенный вариант
from random import *
from types import new_class # * позволяет импортировать все функции
new_array = [i for i in range(10)]
def random_sorting(a):
    for i in range(len(a)-1):
        index = randint(i+1,len(a)-1)
        a[i], a[index] = a[index],a[i]
    return a
print(new_array)
print(random_sorting(new_array))