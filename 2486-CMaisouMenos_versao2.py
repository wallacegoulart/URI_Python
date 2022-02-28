#2486 C MAIS OU MENOS versão 2

dic = {'suco de laranja':120 , 'morango fresco':85 , 'mamao':85
       , 'goiaba vermelha':70 ,'manga':56 , 'laranja':50 ,'brocolis':34 }

while True:
    n = int(input())
    if n == 0:
        break

    consumo = 0 
    for num in range(0,n):
        lista = [x for x in input().split(' ')]
        qnt = int(lista[0])
        alimento = " ".join(lista[1:])

        consumo += dic[alimento]*qnt


    if consumo < 110:
        print(f'Mais {110 - consumo} mg')
    elif consumo > 130:
        print(f'Menos {consumo - 130} mg')
    else:
        print(f'{consumo} mg')
            

