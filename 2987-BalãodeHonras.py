#2987 Balão de Honras

dic ={}
cont = 1
for c in range(65,91):
    dic[chr(c)] = cont
    cont +=1

n = input()

print(dic[n])
