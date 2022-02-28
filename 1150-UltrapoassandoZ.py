#1150 Ultrapassando Z

x = int(input())
while True:
    z = int(input())
    if z > x:
        break

soma = x
cont = 1
for num in range(x+1,z):
    soma += num
    cont +=1 
    if soma > z :
        break

print(cont)    
