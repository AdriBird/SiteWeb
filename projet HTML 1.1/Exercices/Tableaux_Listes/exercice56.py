def couple(val, tab):
    nombre = 0
    for i in range(len(tab)):
        if val == tab[i]:
            nombre += 1
            if val == tab[i+1]:
                print("oui")
            print(True)
            print(nombre)


    else:
        print("La valeur n'est pas dans le tableau")


couple(int(input("Valeur: ")), [2, 3, 5, 5, 1, 3, 8, 3, 6, 3])