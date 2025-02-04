#1047 Tempo de Jogo com Minutos


def tempo_jogo(h_ini, min_ini , h_fim, min_fim):
    """Função calcula o tempo e ja devolve com string"""
    
    #Se for 24 horas 
    if (h_ini == h_fim):

        #Com os minutos iguais
        if (min_ini == min_fim):
            hora = 24
            minuto = 0

        #Com o minutos maior fica 0 hora
        elif min_ini < min_fim:
             hora = 0    
             minuto = min_fim - min_ini

        #Com o minuto menor a hora fica 23
        else:
            hora = 23    
            minuto = (60 - min_ini) + min_fim

    #Se for no mesmo dia 
    elif h_ini < h_fim:

        #Com os minutos menores da hora inicial
        if min_ini < min_fim:
            hora = h_fim - h_ini
            minuto = min_fim - min_ini

        #Com os minutos maior da hora inicial
        else:
            hora = (h_fim - h_ini) - 1 
            minuto = (60 - min_ini) + min_fim


    #Se for no dia posterior
    else:

        #Com os minutos menores da hora inicial
        if min_ini < min_fim:
            hora = (24 - h_ini) + h_fim
            minuto = min_fim - min_ini

        #Com os minutos maior da hora inicial
        else:
            hora = ( (24 - h_ini) + h_fim ) - 1 
            minuto = (60 - min_ini) + min_fim
            
    
    return print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')


#Inicio do programa
h_ini , min_ini , h_fim , min_fim = list(map(int,input().split(' ') ) )

tempo_jogo(h_ini, min_ini , h_fim, min_fim) 
