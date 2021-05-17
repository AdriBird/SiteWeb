def tri_insertion(tab):
    """Permet de trier un tableau du plus petit au plus grand"""
    taille = len(tab)
    cur = 1
    verif = 0
    for cur in range(taille):
        save_cur = tab[cur]
        for verif in range(cur):
            save_verif = tab[verif]
            if save_cur < save_verif:
                tab[verif] = tab[cur]
                tab[cur] = save_verif
    print(tab)






tri_insertion([2,1,3,5,4])