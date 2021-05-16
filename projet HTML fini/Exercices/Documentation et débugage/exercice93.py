#exo 92 nécessaire pour le 93

def est_croissant (t):
    if len(t)==0:
        return None
    i=len(t)-1
    while i>0:
#        print("nouveau tour avec i =" , i)
        if t[i-1]<=t[i]:
            i-=1
        else:
            return False
    return True
assert est_croissant ([1,2,3,4])==True
assert est_croissant ([1,3,2,4])==False
assert est_croissant ([])==None


#exo 93
from random import randint
def tableau_croissant (n):
    t=[0]*n
    a=1
    b=100
    for i in range (n):
        a=randint(a,a+b)
        t[i]=a
    return t

for n in range (2,20):
    for i in range (10):
        t=tableau_croissant (n)
        assert est_croissant(t)