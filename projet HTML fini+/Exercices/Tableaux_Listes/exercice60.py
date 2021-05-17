# Si le programme de l'exercice précédent a été réutilisée
    ## Attention à leur donner des noms différents, sinon c'est une erreur qui est affichée


def pgse(e,tab):
    cur_occ = 1
    max_occ = 0
    occurence = []
    for i in range(len(tab)):
        if i >= 0 and tab[i] != tab[i-1] or tab[i] != e:
            occurence.append(cur_occ)
            cur_occ = 1
        if i >= 0 and tab[i] == e and tab[i] == tab[i-1]:
            cur_occ += 1

    for i in range(len(occurence)):
        if i >= 0 and occurence[i] > occurence[i-1]:
            max_occ = occurence[i]
    return max_occ


def pgs (tab):
    c = 0
    for i in range (len(tab)):
        x = tab[i]
        w = pgse(x,tab)
        if w > c :
            c = w
    return c


print (pgs([6,4,6,6,2,2,2,3,4,5]))




