#1589 Bob Conduite

n = int(input())

for num in range(0,n):
    a,b = [int(x) for x in input().split(' ')]
    print(f'{a+b}')
