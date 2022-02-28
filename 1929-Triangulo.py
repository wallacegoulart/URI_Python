# 1929 Triangulo

lista = [int(x) for x in input().split(' ')]

menor1 = min(lista)
lista.remove(menor1)

menor2 = min(lista)
lista.remove(menor2)

menor3 = min(lista)
lista.remove(menor3)

if (menor1 + menor2) > menor3: 
    print('S')
elif (menor2 + menor3) > min(lista):
    print('S')
else:
    print('N')
