from random import *
def tabaléa(n,a,b):
    tab=[0]*n
    for i in range(n):
        tab[i]=randint(a, b)
    return tab
print(tabaléa(5,1,10))