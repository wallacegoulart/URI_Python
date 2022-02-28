#1153 Fatorial Simples

n = int(input())
fatorial = 1

for num in range(1,n+1):
    fatorial *= num

print(fatorial)
