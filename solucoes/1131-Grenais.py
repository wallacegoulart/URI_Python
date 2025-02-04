# 1131 GRENAIS

vitoria_inter = 0 
vitoria_gremio = 0 
empate = 0 
grenais = 0
while True:

    grenais += 1 
    inter, gremio = list(map(int,input().split(' ') ) )

    if inter > gremio :
        vitoria_inter +=1
    elif inter < gremio :
        vitoria_gremio +=1
    else:
        empate +=1
    
    print("Novo grenal (1-sim 2-nao)")
    validador = int(input())

    if validador == 2:
        break 

print(f'{grenais} grenais')
print(f'Inter:{vitoria_inter}')
print(f'Gremio:{vitoria_gremio}')
print(f'Empates:{empate}')

if vitoria_inter > vitoria_gremio :
    print(f'Inter venceu mais')
elif vitoria_inter < vitoria_gremio :
    print(f'Gremio venceu mais')
else:
    print(f'Nao houve vencedor')
