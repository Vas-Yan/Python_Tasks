# Показать вторую цифру трёхзначного числа
def get_random(min_value, max_value):
    import random
    result = random.randint(min_value,max_value)
    return result
number = get_random(100,1000)
import math
print(str("number = "), number, str("second digit = "),math.floor(number%100/10))