#1234 Senteça Dançante


while True:
    try:
        n = input()
        lista = []
        for x in n:
            lista.append(x)
        index = 0
        index2 = 0
        for value in lista:
            if index % 2 == 0 :
                print(lista[index2].upper(),end='')
            else:
                print(lista[index2],end='')

            if lista[index2] != ' ':
                index += 1

            index2 += 1          
        print()  
    except EOFError:
        break

