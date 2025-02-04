#1199 Conversão SImples de Base

lista =[]
while True:
    n = input()
    try:
        lista.append(int(n))
        if int(n) < 0:
            break
    except ValueError:
        lista.append(n)


lista.pop()

for num in lista:

    try:
        print(str(hex(num).upper()).replace('X','x'))

    except (TypeError,ValueError):
        print(str(int(num,16)).upper())
