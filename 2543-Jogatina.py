#2543 Jogatina UFPR


while True:
    try:
        n , id = [int(x) for x in input().split(' ')]
        contador = 0
        for num in range(0,n):
            id2, t = [int(x) for x in input().split(' ')]
            if id == id2 and  t == 0  :
                contador +=1
        print(contador)  
    except EOFError:
        break
 
      
