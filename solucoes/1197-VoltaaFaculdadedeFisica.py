#1197 Volta a Faculdade de Fisica

while True:
    
    try:
        n , m = [int(x) for x in input().split(' ')]
        print(f'{n*2*m}')
            
        

    except EOFError:
        break
