# Resto da Divisão

def ordena(x,y):
    if x > y :
        a = x
        x = y
        y = a
        
    return x , y

x = int(input())
y = int(input())
x,y = ordena(x,y)
x +=1
while x < y :
    
    if x % 5 == 2 or x % 5 == 3 :
        print(x)

    x += 1
