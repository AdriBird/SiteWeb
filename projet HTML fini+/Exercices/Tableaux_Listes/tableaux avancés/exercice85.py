#exo 85
import random
def exo85(a):
    t=[[random.randint(1,9999) for j in range (a)] for i in range (a)]
    m=t[0][0]
    for i in range (a):
        for j in range (a):
            if t[j][i]>m:
                m=t[j][i]
    return t,m

