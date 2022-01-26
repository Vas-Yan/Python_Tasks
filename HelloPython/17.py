# По двум заданным числам проверять является ли одно квадратом другого
import Random_Numbers
a = Random_Numbers.get_random(4,10)
b = Random_Numbers.get_random(1,3)
def check_whether_square (a,b):
    result = True
    if a == b*b:
        result = True
    else:
        result = False
    return result
print (a,b,check_whether_square(a,b))