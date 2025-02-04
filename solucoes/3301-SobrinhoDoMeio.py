#3301 Sobrinho do Meio

h,z,l = list(map(int,input().split()))

if (h > z and h < l) or (h > l and h < z):
    print('huguinho')

elif (z > h and z < l) or (z > l and z < h):
    print('zezinho')

else:
    print('luizinho')      
