#1199 Conversão Simples de Base

lista = []
validador = True 
while validador:
    n = input()
    lista.append(n)
    print(n,n.isdigit())
    if n.isdigit() and int(n) < 0 :
        print('passou aqui')
        validador = False     

print(lista)
