#1847 Bem-Vindos e Bem-Vindas ao Inverno

a,b,c = [int(x) for x in input().split(' ')]

if a > b and (b == c or b < c):
    print(':)')

elif a < b and (b == c or b > c):
    print(':(')

elif a < b and b < c and ( abs(b-a) > abs(c-b)):
    print(':(')

elif a < b and b < c and(abs(b-c) >=  abs(b-a)):
    print(':)')

elif a > b and b > c and (abs(b-c) < abs(a-b)):
    print(':)')

elif a > b and b > c and (abs(b-c) >= abs(b-a)):
    print(':(')

elif a == b:
    if  b < c:
        print(':)')
    else:
        print(':(')
    
