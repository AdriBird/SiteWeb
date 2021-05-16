'''
a) La fonction permet de trouver l'indice du nombre le plus grand dans le tableau t
b) On peut changer le nom de la variable m par indice_maximum et t par tab et changer le nom de la fonction par
indice_maximum_tableau
'''
def maximum_tableau(t):
    """
    Renvoie l'indice maximum du tableau t
    """
    assert len(t) > 0 , "COMPLETE OR PERISH"
    m = 0
    for i in range(len(t)):
        if t[i] > t[m]:
            m = i
    print(m)
    return m
maximum_tableau(["oui"])

assert maximum_tableau([0,1,2,3,4,5,6,7,8,9])==9, "non"
assert maximum_tableau([9,8,7,6,5,4,3,2,1,0])==0, "non"
#assert maximum_tableau([0,0,0,0])==0, "mêmes nombres"
assert maximum_tableau((["oui"]))==0, "string"

'''
c) on constate qu'il renvoie quand même l'indice 0 alors que le tableau n'a pas de contenu
'''
