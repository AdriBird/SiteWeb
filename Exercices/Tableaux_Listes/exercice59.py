def pgs(e,tab):
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

print(pgs(1, [6,6,6,2,3,4,5]))

