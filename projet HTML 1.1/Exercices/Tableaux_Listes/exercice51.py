
'''
def copie(tab):
    copie_tab = tab
    return copie_tab

print(copie([1, 2, 3]))'''


























def copie(tab):
    copie_tab=[0]*len(tab)
    for i in range(len(tab)):
        copie_tab[i]=tab[i]