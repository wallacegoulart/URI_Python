#1046 Tempo de Jogo

def tempo_jogo(ini, fim):
    """Contablizar o tempo de jogo"""

    if ini < fim :
        return fim - ini 

    elif ini == fim :
        return 24

    else:
        return (24 - ini) + fim 


#Inicio do programa 
hora_inicial , hora_final = list(map(int,input().split(' ') ) )

tempo = tempo_jogo(hora_inicial , hora_final)

print(f'O JOGO DUROU {tempo} HORA(S)')
