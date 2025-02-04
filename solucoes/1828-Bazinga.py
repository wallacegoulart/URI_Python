#1828 Bazinga

n = int(input())

for num in range(1,n+1):
    s,r = input().split(' ')

    if r == s:
         print(f'Caso #{num}: De novo!')    
    
    elif s == 'tesoura':
        if r == 'papel' or r =='lagarto':
            print(f'Caso #{num}: Bazinga!')
        else:
            print(f'Caso #{num}: Raj trapaceou!')    

    elif s =='papel':
        if r =='pedra' or r =='Spock' :
            print(f'Caso #{num}: Bazinga!')
        else:
            print(f'Caso #{num}: Raj trapaceou!')    
    
    elif s =='pedra':
        if r =='lagarto' or r =='tesoura' :
            print(f'Caso #{num}: Bazinga!')
        else:
            print(f'Caso #{num}: Raj trapaceou!')    


    elif s =='lagarto':
        if r =='Spock' or r =='papel' :
            print(f'Caso #{num}: Bazinga!')
        else:
            print(f'Caso #{num}: Raj trapaceou!')    


    elif s =='Spock':
        if r =='pedra' or r =='tesoura' :
            print(f'Caso #{num}: Bazinga!')             
        else:
            print(f'Caso #{num}: Raj trapaceou!')    

   
