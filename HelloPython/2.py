# По двум заданным числам проверять является ли первое квадратом второго
def random_number (min_value, max_value):
    import random
    R = random.randint(min_value, max_value)
    return R
a = random_number(0,10)
b = random_number(0,10)
def check (a,b):
     result = True
     if a == b*b: 
         result = True
     else:
         result = False
     return result
print(a, b, check(a,b))