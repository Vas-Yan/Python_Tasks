# Показать числа от -N до N
import random
from this import s
N = random.randint(1,10)
print(N)
def show_numbers (N):
    a = range(-N,N+1)
    s = " "
    for i in a:
        s = s + str(i) + '; '
    return s
print(show_numbers(N))