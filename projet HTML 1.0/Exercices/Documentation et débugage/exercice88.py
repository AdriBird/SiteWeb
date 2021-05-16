#exo 88

def max_tableau (t):
    """Cette fonction renvoie l'indice de la valeur maximale du tableau.
    Attention, ne pas utiliser de tableau vide."""
    m=0
    for i in range (len(t)):
        if t[i]>t[m]:
            m=i
    return m

