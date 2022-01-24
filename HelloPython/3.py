# Даны два числа. Показать большее и меньшее число
def get_random (min_value, max_value):
    import random
    result = random.randint(min_value,max_value)
    return result
a = get_random(0,100)
b = get_random(0,100)
print(a, b , "max =", max(a,b),"min =", min(a,b))