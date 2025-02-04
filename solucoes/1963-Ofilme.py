#1963 o Filme

n,m = [float(x) for x in input().split(' ')]
if n == m :
    print('0.00%')
else:
    print('{:.2f}%'.format( (m/n*100)-100))
