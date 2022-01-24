# Найти максимальное из трех чисел
def get_random (min_value, max_value):
    import random
    result = random.randint(min_value, max_value)
    return result
a = get_random (0,100)
b = get_random (0,100)
c = get_random (0,100)
print(a,b,c,max(a,b,c))