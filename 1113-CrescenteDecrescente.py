# 1113 Crescente e Decrescente

while True:

    x,y = list(map(int,input().split(' ')  ) )
    
    if x < y :
        print('Crescente')

    elif x > y :
        print('Decrescente')

    else:
        break
