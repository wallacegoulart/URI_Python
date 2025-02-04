# 1099 Soma de Impares Consecutivos II

tamanho = int(input())
cont = 0


while cont < tamanho :
    soma = 0
    a,b = list(map(int,input().split(' ') ) )

    if a > b:
        x = a
        a = b
        b = x
    
    for num in range(a+1,b):
        if num % 2 != 0:
            soma += num
    cont += 1
    print(soma)        
