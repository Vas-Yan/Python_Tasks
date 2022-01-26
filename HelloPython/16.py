# Дано число обозначающее день недели. Выяснить является номер дня недели выходным
Sunday = 1
Monday = 2
Tuesday = 3
Wednesday = 4
Thursday = 5
Friday = 6
Saturday = 7
from operator import truediv
from tabnanny import check
import Random_Numbers
given_number = Random_Numbers.get_random(1,7)
def check_wether_weekend(number):
    result = True
    if given_number == 1 or given_number == 7:
        result = True
    else:
        result = False
    return result
print(given_number, check_wether_weekend(given_number))