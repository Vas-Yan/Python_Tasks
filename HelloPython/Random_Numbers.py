# Написать генератор случайных чисел
def get_random (min_value, max_value):
    import random
    result = random.randint(min_value, max_value)
    return result