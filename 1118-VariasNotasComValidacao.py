# 1118 Varias Notas Com Validação

media = 0
cont = 0
novo_calculo = 1
while True:

    while cont < 2:
        nota = float(input())

        if nota > 10 or nota < 0:
            print('nota invalida')
        else:
            media += nota
            cont +=1

    if novo_calculo == 1: 
        print("media = {:.2f}".format(media/2) )


    print("novo calculo (1-sim 2-nao)")
    novo_calculo = int(input())
    
    if novo_calculo == 2:
        break

    elif novo_calculo == 1:
        media = 0
        cont = 0
                
