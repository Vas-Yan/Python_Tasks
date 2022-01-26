# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import Random_Numbers
import math
number = Random_Numbers.get_random(10,100)
print(number)
def show_bigger_digit(number):
    result = 0
    if number%10 > math.floor(number/10):
        result = number%10
    else:
        result = math.floor(number/10)
    return result
print(show_bigger_digit(number))