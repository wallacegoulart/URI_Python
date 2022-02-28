#1962 Há Muito, Muito Tempo Atras

n = int(input())

for num in range(0,n):
    ano = int(input())
    if ano > 2015:
        print(f'{ano-2014} A.C.')
    elif ano == 2015:
        print(f'{1} D.C.')
    else:
        print(f'{2015-ano} D.C.')
