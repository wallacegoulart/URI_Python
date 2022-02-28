#1101 Squencia de Numeros e Soma

while True:
    a,b = list(map(int,input().split(' ') ) )
    soma = 0
    lista =[]
    if b <= 0 or a <= 0 :
        break
        
    if a > b:
        x = a
        a = b
        b = x
            
    for num in range(a,b+1):
        soma += num
        lista.append(num)

    for num1 in lista:
        print(f'{num1} ',end="")

    print(f'Sum={soma}',end="")
    print()

        
