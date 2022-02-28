#1094 Experiência

tamanho = int(input())
i = 0
coelho = 0
sapo = 0 
rato = 0
total = 0

while i < tamanho:
    i += 1
    
    num , tipo = input().split(' ')
    num = int(num)

    total += num

    if tipo.lower() == 'c':
        coelho += num

    elif tipo.lower() == 'r':
        rato += num

    elif tipo.lower() == 's':
        sapo += num


print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print("Percentual de coelhos: {:.2f} %".format( float(coelho/total*100) ) )
print("Percentual de ratos: {:.2f} %".format( float(rato/total*100) ) )        
print("Percentual de sapos: {:.2f} %".format( float(sapo/total*100) ) )
