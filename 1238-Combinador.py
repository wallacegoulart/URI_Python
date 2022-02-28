# 1238 Combinador

n = int(input())

for i in range(0,n):
    s = [num for num in input().split(' ')]
    dic1={}
    dic2 = {}

    
    index = 0
    for i in s[0]:
        dic1[index] = i
        index +=1


    index = 0
    for i in s[1]:
        dic2[index] = i
        index +=1


    if len(dic1) >= len(dic2):
        t = len(dic1)
    else:
        t = len(dic2)


    nova_string = []
    for num in range(0,t):
        nova_string.append(dic1.get(num,''))
        nova_string.append(dic2.get(num,''))



    for value in nova_string:
        if value != '':
            print(value,end="")
    print()        

    
    
