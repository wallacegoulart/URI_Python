#1789 A Corrida de Lesma


while True:

    try:
        n = int(input())
        lista = input().split(' ')
        lista2=[]
        for num in lista:
            lista2.append(int(num))

            
        maior = max(lista2)

        if maior >= 20:
            print('3')
        elif maior >=10 and maior < 20 :
            print('2')
        else:
            print('1')
         
        

    except EOFError:
        break
