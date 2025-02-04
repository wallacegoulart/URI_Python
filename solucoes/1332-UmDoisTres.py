# 1332 Um-Dois-Tres

n = int(input())
one = ['o','n','e']
for num in range(0,n):
    m = input()
    if len(m) >= 5 :
        print(3)

    else:
        cont = 0
        i = 0 
        for value in m:
            if value == one[i]:
                cont +=1
            i +=1
                
        if cont > 1:
            print(1)
        else:
            print(2)
            
            
            
        
