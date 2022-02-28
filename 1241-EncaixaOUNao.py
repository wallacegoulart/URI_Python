#1241 EncaixaOUNao
n = int(input())
for i in range(0,n):
    lista = [num for num in input().split(' ')]

    if lista[1] not in lista[0]:
        print('nao encaixa')
        break

    
    else:
        lista1 = lista[0]
        lista2 = []
        index = - len(lista[1])
        for num in lista1[index:]:
            lista2.append(num)

        nova_lista = "".join(lista2)

        if lista[1] == nova_lista:
            print('encaixa')
        else:
            print('nao encaixa')
            
