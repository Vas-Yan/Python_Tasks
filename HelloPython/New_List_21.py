# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет
a = ["123", "234", "123", "234", "567", "123"]
b = "123"
if a.index(b)>-1:
    a.remove(a[a.index(b)])
if (b in a) == False:
    print(str("no second repeat"))
else: print(a.index(b)+1)
