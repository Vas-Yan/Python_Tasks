# Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
a = input(str( "-->"))
b = input(str( "-->"))
def search_one_in_two(a,b):
    if (a in b):
        count = 0
        setting = ''
        for i in range(len(b)-len(a)+1):
            for j in range(len(a)):
                setting = setting + b[i+j]
            if (setting==a):
                count += 1
                setting = ''
        return count
    else:
        return False
print(search_one_in_two(a,b))