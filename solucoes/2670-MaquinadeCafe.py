#2670 Máquina de Cafe

a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1 > a2 and a1 > a3:
    print(f'{a3*4 + a2*2 }')
elif a2 > a1 and a2 > a3:
    print(f'{a3*2 + a1*2}')
else:
    print(f'{a1*4 + a2*2}')
