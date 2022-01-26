# Выяснить, кратно ли число заданному, если нет, вывести остаток.
import Random_Numbers
import math
original_number = Random_Numbers.get_random(1,100)
given_number = Random_Numbers.get_random(1,10)
def check_for_multiplicity(numbers):
    result = 0
    if original_number % given_number == 0:
        result = True
    else:
        result = original_number / given_number - math.floor(original_number / given_number)
    return result
print(original_number,  given_number, check_for_multiplicity(original_number))
