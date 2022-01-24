# Выяснить является ли число чётным
def get_random (min_value, max_value):
    import random
    result = random.randint(min_value, max_value)
    return result
number = get_random(0,100)
print(str("number ="), number)
def check_if_even(number):
    s = True
    if number % 2 == 0:
        s = True
    else:
        s = False
    return s
print(str("number is odd? "), check_if_even(number))