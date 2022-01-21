from cgitb import text


#print('Hello World')
# value = None
# a = 123
# b = 1.23
# value = 'idiot'
# print(type(a))
# print(type(b))
# print(type(value))
# s= 'idiot'
# print(s) # вывод строки
# print(f'{a} - {b} - {s}')
# list = [1,2,3]
# print(list)
username = input('введите имя ')
if username == "Маша":
    print ("Ура, это же Маша")
elif username == 'Марина':
    print ("я так ждал тебя, Марина!")
else:
    print("Привет, ", username)