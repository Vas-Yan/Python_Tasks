# Написать программу получающую набор произведений чисел от 1 до N
from itertools import product
import Random_Numbers
n = Random_Numbers.get_random(0,10)
def product_of_N(n):
    a = 1
    result = []
    for i in range(1,n+1):
        a = i*a
        result.append(a)
    return result
print(n,product_of_N(n))