import math


def bond_value (V0, r, n, M, c):
    
    
    if (c==1):
    
    
      Vn = V0 * math.exp(r*n)
      return Vn

    elif (c==0):
      Vn = V0 * math.pow(1+(r/M),n * M)
      return Vn
    else:
      print('error')
    
#parameters

V0 = 1000
r = 0.05
n = 10
M = 4
c = 0

print(bond_value(V0, r, n, M, c))
    