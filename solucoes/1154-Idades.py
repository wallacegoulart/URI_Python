#1154 Idades

soma = 0
cont = 0
while True:
    idade = int(input())
    if idade < 0 :
        break
    else:
        soma +=idade
        cont +=1

print("{:.2f}".format(soma/cont))        
