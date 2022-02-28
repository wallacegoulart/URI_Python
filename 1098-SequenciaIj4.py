#1098 Sequencia IJ4

i = 0.0

while i <= 1.8:

    cont = 0
    j = 1
    while cont < 3:
        if i == 0 or i == 1.0 or i == 2.0:
            print('I={:.0f} J={:.0f}'.format(i,i+j) )
        else:
            print('I={:.1f} J={:.1f}'.format(i,i+j) )
            
        j += 1
        cont +=1
        
    i += 0.2         



i += 0.2
cont = 0
j = 1
while cont < 3:
    print('I={:.0f} J={:.0f}'.format(i,i+j) )
    j += 1
    cont +=1
