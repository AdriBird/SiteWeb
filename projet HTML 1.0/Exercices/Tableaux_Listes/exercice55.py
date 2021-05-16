def nb_occurences(val, tab):
    nombre = 0
    for i in range(len(tab)):
        if val == tab[i]:
            nombre += 1
            print(True)
            print(nombre)


    else:
        print("La valeur n'est pas dans le tableau")

nb_occurences(int(input("Valeur: ")), [2, 3, 5, 7, 1, 3, 8, 3, 6, 3])