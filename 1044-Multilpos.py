#1044_Multiplos

a , b = list(map(int,input().split(' ') ) )

if a % b == 0:
    print('Sao Multiplos')

elif b % a == 0 :
    print('Sao Multiplos')

else:
    print('Nao sao Multiplos')
    
