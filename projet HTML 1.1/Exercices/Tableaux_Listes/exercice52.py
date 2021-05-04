#à faire

def echange(tab, i, j):
    savei = i
    savej = j
    tab[i]=tab[savej]
    tab[j]=tab[savei]
    print(tab)
    print(savei, savej)
echange([1, 2, 3, 4, 5, 6], 1, 4)
