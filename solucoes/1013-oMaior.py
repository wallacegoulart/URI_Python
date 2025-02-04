a,b,c = [int(x) for x in input().split()]
y = (a+b + abs(a-b))/2
z = (y+c + abs(y-c))/2
print("%d eh o maior" %z)
