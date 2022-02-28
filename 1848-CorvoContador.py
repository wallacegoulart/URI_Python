#1848 Corvo Contador

grito = 0
valor = 0
while grito < 3:
    n = input().split(' ')
    if 'caw'in n:
        grito +=1
        print(valor)
        valor = 0
    else:
        n = "".join(n).replace('-','0').replace('*','1')
        n = int(n,2)
        valor += n 

    
  
