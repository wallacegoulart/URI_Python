#1973 Jornada nas Estrelas

n = int(input())
lista = [int(x) for x in input().split(' ')]
total = sum(lista)
roubados = 0
maximo = len(lista)

i = 0
antes = lista[i]

while True:
    if lista[i] > 1:
        roubados +=1
        antes = lista[i]
        lista[i] -=1

    if antes == 0 :
        break
    elif antes % 2== 0 :
        i -=1
        
    else :
        i +=1

    if i == len(lista) or i < 0:
        break 

print(total-roubados)
