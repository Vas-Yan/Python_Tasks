# Написать программу вычисления значения функции y = f(a)
from tkinter import N


def get_random(min_value, max_value):
    import random
    result = random.randint(min_value,max_value)
    return result
b = get_random(0,10)
k = get_random(0,10)
a = get_random(0,10)
def function(a):
    y = k*a+b
    return y
print(str ("a ="), a, str("k ="), k,str("b ="),b)
str('/n')
print(str ("f(a) = k*a + b"))
str('/n')
print(str ("f(a) ="), function(a))