#3175 Grupo de Trabalho do Noel

cont = int(input())
boneco = 0
arquiteto = 0
musico = 0
desenhista = 0 

for i in range(0,cont):
    nome , grupo , horas = input().split(' ')
    horas = int(horas)

    if grupo == 'bonecos':
        boneco += horas

    elif grupo == 'arquitetos':
        arquiteto += horas

    elif grupo == 'musicos':
        musico += horas

    elif grupo == 'desenhistas':
        desenhista += horas


brinquedo = 0
brinquedo += boneco // 8
brinquedo += arquiteto // 4
brinquedo += musico // 6
brinquedo += desenhista // 12
print(brinquedo)

        
