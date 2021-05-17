def appartient(val, tab):
    for i in range(len(tab)):
        if val == tab[i]:
            print("La valeur est dans le tableau")
            break
    else:
        print("La valeur n'est pas dans le tableau")

appartient(int(input("Valeur: ")), [1, 2, 3, 4, 5, 6])