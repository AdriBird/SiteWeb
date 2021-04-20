

def naissance_mois (d):
    d_nb_mois = {}
    t = list (d.values())
    for element in t:
        if element in d_nb_mois:
            d_nb_mois[element] += 1
        else:
            d_nb_mois[element] = 1
    return d_nb_mois