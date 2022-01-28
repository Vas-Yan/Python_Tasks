# Подсчитать сумму цифр в вещественном числе
a = 8.11111
def sum_of_digits(a):
    result = 0
    b = str(a)
    for i in b:
        if i != ".":
            result += int (i)
    return result
print(a,sum_of_digits(a))