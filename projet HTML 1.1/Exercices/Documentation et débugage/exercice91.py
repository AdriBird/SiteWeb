#exo 91

def max_tableau91 (t):
    """Cette fonction renvoie l'indice de la valeur maximale du tableau.
    Attention, ne pas utiliser de tableau vide.
    Mettre print(max_tableau90 (t)) si on veut que ça renvoie "None" """
    if len(t)==0:
        return None
    m=0
    for i in range (len(t)):
        if t[i]>t[m]:
            m=i
    return m
assert max_tableau91 ([3,5,9,4,7,9,13,15,10])==7
assert max_tableau91 ([1,2,3,4,5,6,7,8,9])==8
assert max_tableau91 ([])==None