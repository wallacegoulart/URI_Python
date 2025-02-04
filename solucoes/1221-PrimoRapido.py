# 1221 Primo Rapido

n = int(input())
for num in range(0,n):
    primo = int(input())
    for i in range(2,primo//2):
        if primo % i == 0:
            print("Not Prime")
            break
