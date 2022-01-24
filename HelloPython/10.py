# Показать последнюю цифру трёхзначного числа
def get_random (min_value, max_value):
    import random
    result = random.randint(min_value,max_value)
    return result
number = get_random(100,1000)
print(number)
print(str("last digit"),number%10)