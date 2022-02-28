#1983 O escolhido

n = int(input())
id_maior = 0
nota_maior = 0 

for num in range(0,n):
    id , nota = [float(x) for x in input().split(' ')]
    if nota >= nota_maior:
        nota_maior = nota
        id_maior = id

if nota_maior >= 8:
    print(int(id_maior))
else:
    print('Minimum note not reached')
