# Найти максимальное из трех чисел
def max_from_three (x, y, z):
    max = x
    if max < y: max = y
    if max < z: max = z
    return max
print(max_from_three(10, -10, 1))
import random
x = random.randint(1, 100)
y = random.randint(1, 100)
z = random.randint(1, 100)
print(x, y, z)
print(max_from_three(x, y, z))