#exo 90

def max_tableau90 (t):
    """Cette fonction renvoie l'indice de la valeur maximale du tableau.
    Attention, ne pas utiliser de tableau vide.
    Mettre print(max_tableau90 (t)) si on veut que le programme renvoie "None" """
    if len(t)==0:
        return None
    m=0
    for i in range (len(t)):
        if t[i]>t[m]:
            m=i
    return m