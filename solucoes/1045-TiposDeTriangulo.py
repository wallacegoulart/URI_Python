#1045_Tipos_Triangulo


def triangulo(lista):

    if lista[0] >= lista[1] + lista[2]:
        print('NAO FORMA TRIANGULO')

    else:
        if (lista[0]**2) == (lista[1]**2) + (lista[2]**2):
            print('TRIANGULO RETANGULO')

        if (lista[0]**2) > (lista[1]**2) + (lista[2]**2):
            print('TRIANGULO OBTUSANGULO')

        if (lista[0]**2) < (lista[1]**2) + (lista[2]**2 ):
            print('TRIANGULO ACUTANGULO')

        if lista[0] == lista[1] == lista[2]:
            print('TRIANGULO EQUILATERO')

        if (lista[0] == lista[1] and lista[2] != lista[0]) or  (lista[2] == lista[1] and lista[0] != lista[1] ) or (lista[2] == lista[0] and lista[0] != lista[1]) :
            print('TRIANGULO ISOSCELES')


a , b, c = list(map(float,input().split(' ') ) )
lista = [ a, b, c ]
lista.sort(reverse=True)

triangulo(lista)
