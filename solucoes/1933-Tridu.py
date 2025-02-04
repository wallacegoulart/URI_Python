#1933 Tri-du

n, m = [int(x) for x in input().split(' ')]

if n == m :
    print(n)
else:
    print(n if n > m  else m)
    
