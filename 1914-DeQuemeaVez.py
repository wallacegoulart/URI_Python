#1914 De Quem é a VEz

n = int(input())

for num in range(0,n):
    lista = [x for x in input().split(' ')]
    a , b = [int(x) for x in input().split(' ')]
    jogador1 = lista[0]        
    escolha1 = lista[1]
    jogador2 = lista[2]
    escolha2 = lista [3]

    if (a+b)%2 == 0:
        if escolha1.lower() == 'par':
            print(jogador1)
        else:
            print(jogador2)

    else:
        if escolha1.lower() == 'impar':
            print(jogador1)
        else:
            print(jogador2)

            
        
    
