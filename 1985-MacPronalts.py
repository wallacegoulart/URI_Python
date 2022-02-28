#1985 MacPronalts

dic = {1001: 1.50 , 1002:2.50 , 1003:3.50 , 1004:4.50 , 1005:5.50}

n = int(input())
total = 0.00

for num in range(0,n):
    key,qtd = [int(i) for i in input().split(' ')]

    total += dic[key] * qtd


print('{:.2f}'.format(total))

