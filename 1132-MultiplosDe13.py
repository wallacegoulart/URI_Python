# 1132 Multiplos de 13

def ordena(x,y):
    if x > y:
        a = x
        x = y
        y = a

    return x , y         
        
x = int(input())
y = int(input())
soma = 0
x , y = ordena(x,y)

while x <= y :
    if x % 13 != 0 :
        soma += x

    x +=1

print(soma)     
