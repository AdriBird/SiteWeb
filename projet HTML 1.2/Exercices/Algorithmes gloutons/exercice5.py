def monnaie(somme, euro):
    fini = False
    nombre_de_piece = 0
    type_de_piece = []
    somme_hypothetique = 0
    while fini == False:
        for i in range(len(euro)):
            if euro[i] > somme:
                nombre_de_piece += 1
                type_de_piece.append(euro[i])
                somme_hypothetique += euro[i]
            if euro[i] == somme:
                nombre_de_piece += 1
                type_de_piece.append(euro[i-1])
                somme_hypothetique += euro[i-1]
                return nombre_de_piece, type_de_piece
            if somme_hypothetique == somme:
                fini = True

        return [nombre_de_piece, type_de_piece]

def mise_en_scene(somme, euro):
    print("Il faudra rendre", monnaie(somme, euro), "pièces, avec", )
mise_en_scene(9, [1, 2, 5, 10, 20, 100, 200])