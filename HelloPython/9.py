# Показать четные числа от 1 до N
import random
N = random.randint(1,100)
print(N)
def show_odd_num (N):
    a = range(1,N+1)
    s = ''
    for i in a:
        if i % 2 == 0:
            s = s + str(i)+"\n"
    return s
print(show_odd_num(N))


# a =  range(1,N)
# for i in a:
#     if i%2 == 0:
#         print(i)