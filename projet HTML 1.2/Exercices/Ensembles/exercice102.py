

def doublon(t):
    ensemble = set ()
    for e in t:
        if e in ensemble:
            return True
        else:
            ensemble.add (e)
    return False

def paradox_des_aniversaires(p):
    compteur = 0
    for i in range (100):
        t = [randint(1, 365) for j in range (p)]
        if doublon(t):
            compteur += 1
    return compteur