#1198 O Bravbo Guerreiro Hashmat

while True:

    try:
        n,m = [int(x) for x in input().split(' ')]
        print('{}'.format(abs(n-m)))

    except EOFError:
        break
