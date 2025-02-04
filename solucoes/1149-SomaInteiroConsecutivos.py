#1149 Soma de Inteiro COnsecutivos

lista = input().split(' ')
a = int(lista[0])

for num in lista[1:]:
    if int(num) > 0:
        n = int(num)
        break
soma = 0
for i in range(0,n):
    soma += i+a

print(soma)
