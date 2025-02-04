#1144 Sequencia Lógica

x = int(input())
a = 1
b = 1
c = 1
d = 2
for num in range(1,x*2+1):

    print(f'{a} {b} {c}')

    if num % 2 == 0:
        a +=1
        b += d
        c = a * b
        d += 2
    else:
        b+=1     
        c+=1


