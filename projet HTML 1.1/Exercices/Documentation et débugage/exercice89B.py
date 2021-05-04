#exo 89 partie B

def max_tableaub (t):
    """Cette fonction renvoie l'indice de la valeur maximale du tableau.
    Attention, ne pas utiliser de tableau vide."""
    assert len(t)>0 , "On ne peut pas utiliser un tableau vide!"
    m=0
    for i in range (len(t)):
        if t[i]>t[m]:
            m=i
    return m

