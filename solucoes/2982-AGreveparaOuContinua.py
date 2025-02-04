#2982 A greve para ou Continua

n = int(input())
governo = 0
gasto = 0
for num in range(0,n):
    a,b = input().split(' ')
    b = int(b)

    if a == 'V':
        governo += b

    else:
        gasto += b



if governo >= gasto :
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
         
