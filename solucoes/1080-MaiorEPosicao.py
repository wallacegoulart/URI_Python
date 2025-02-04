#108 Maio e Posição

i = 0
maximo = 0
pos = 0
while i < 100:
    i += 1
    n = int(input())
    
    if n > maximo:
        maximo  = n
        pos = i
    

print(f'{maximo}')
print(f'{pos}')
    
    
