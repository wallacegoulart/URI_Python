#2486  C mais ou Menos ?

while True:
    n = int(input())
    if n == 0:
        break

    consumo = 0
    for num in range(0,n):
        lista = input().split(' ')
        qnt = int(lista[0])
        alimento = " ".join(lista[1:])


        
        if alimento == 'suco de laranja':
            consumo += (120 * qnt)
        elif alimento == 'morango fresco':
            consumo += (85 * qnt)
        elif alimento == 'mamao':
            consumo += (85 * qnt)
        elif alimento == 'goiaba vermelha':
            consumo += (70 * qnt)
        elif alimento == 'manga':
            consumo += (56 * qnt)   
        elif alimento == 'laranja':
            consumo += (50 * qnt)
        elif alimento == 'brocolis':
            consumo += (34 * qnt)

    if consumo < 110:
        print(f'Mais {110-consumo} mg')
    elif consumo > 130:
        print(f'Menos {consumo-130} mg')
    else:
       print(f'{consumo} mg') 
