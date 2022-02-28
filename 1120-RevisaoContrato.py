#1120 Revisão de Contrato

while True:
    n ,x = [int(x) for x in input().split(' ')]
    if n == 0 and x == 0:
        break

        
    lista = [v for v in str(x)]

    while str(n) in lista:
        lista.remove(str(n))

    if len(lista) == 0:
        lista.append('0')

        
    num_final = "".join(lista[:])
    print(int(num_final))

    


    
