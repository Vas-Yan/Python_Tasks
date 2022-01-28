# Подсчитать сумму цифр в вещественном числе
a = 8.11111
def sum_of_digits(a):
    result = 0
    b = str(a)
    for i in range (0, len(b)):
        if b[i] != ".":
            result += int(b[i])
    return result
print(a, sum_of_digits(a))