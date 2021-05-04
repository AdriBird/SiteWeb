#exo 89 partie A

def max_tableau (t):
    """Cette fonction renvoie l'indice de la valeur maximale du tableau.
    Attention, ne pas utiliser de tableau vide."""
    if len(t)==0:
        exit("max_tableau : Cette fonction renvoie l'indice de la valeur maximale du tableau. Attention, ne pas utiliser de tableau vide.")
    m=0
    for i in range (len(t)):
        if t[i]>t[m]:
            m=i
    return m


