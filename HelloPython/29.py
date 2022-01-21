# Написать программу вычисления произведения чисел от 1 до N
import random
from unittest import result
N = random.randint(1,10)
print(N)
def multiple_1_to_N(N):
    a = range(1,N+1)
    result = 1
    for i in a:
        result = result*i
    return result
print(multiple_1_to_N(N))

    