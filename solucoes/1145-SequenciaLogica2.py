#1145 Sequencia logica

x,y = list(map(int,input().split(' ')))

for num in range(1,y+1,x):
    for num1 in range(0,x):
        if num1 != x-1:
            print(f'{num+num1}',end=' ')
        else:
             print(f'{num+num1}',end='')
   
    if num+2 == y:
        break
    print()
    
