#1146 SEQUANCIAS CRESCENTES


while True :
    x = int(input())
    if x == 0 :
        break

    for num in range(1,x+1):
        if num != x :
            print(num,end=' ')
        else:
            print(num,end='')
