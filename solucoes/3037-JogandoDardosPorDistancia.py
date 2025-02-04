#3037 Jogando Dardos Por Distancia

jogos = int(input())

for num in range(0,jogos):
    pontos_joao = 0
    pontos_maria = 0
    for i in range(0,6):
        x , d = [int(x) for x in input().split(' ')]
        if i < 3:
             pontos_joao = pontos_joao + (x*d)
        else:
            pontos_maria = pontos_maria + (x*d)


    if pontos_joao > pontos_maria:
        print('JOAO')
    else:
        print('MARIA')
