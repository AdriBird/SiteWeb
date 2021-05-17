def min(ligne):
    minim=ligne[0]
    for i in range(1,len(ligne)):
        if minim>ligne[i]:
            minim=ligne[i]

def max_du_min():
    max=min(tab[0])
    for i in range(len(tab)):
        if min(tab[i])>max:
            max=min(tab[i])
        print(max)
