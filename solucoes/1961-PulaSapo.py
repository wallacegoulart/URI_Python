#1961 Pula Sapo

p,n = [int(x) for x in input().split(' ')]
lista = [int(x) for x in input().split(' ')]
a = True
for num in range(1,n):
    if lista[num-1] + p < lista[num]:
        a = False
        break
    
if a:
    print('YOU WIN')
else:
    print('GAME OVER')
