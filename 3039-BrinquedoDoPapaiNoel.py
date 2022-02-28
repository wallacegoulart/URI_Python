#3039 Brinquendo do Papai Noel

i = int(input())
carrinho = 0
boneca = 0 

for num in range(0,i):
    nome , genero = input().split(' ')

    if genero == 'M':
        carrinho +=1
    else:
        boneca +=1


print(f'{carrinho} carrinhos')
print(f'{boneca} bonecas')
