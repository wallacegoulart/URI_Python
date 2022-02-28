#1240 Enacaixa Ou Nao

n = int(input())
for num in range(0,n):
    a,b = input().split(' ')
    tam = -1 - len(b)

    if b == a[tam+1:]:
        print('encaixa')
    else:
        print('nao encaixa')
    
