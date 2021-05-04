from random import *

def jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(nombre):
    run = True
    while run:
        if nombre < 0:
            phrase = randint(1, 5)
            if phrase == 1:
                print("Mec tu fais chier bordel passe moi un nombre positif")
                jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(
                    int(input("Choisis un nombre positif stp (surtout pas de nombre négatifs sinon je te goume")))
            if phrase == 2:
                print("Maiiis euuuh passe moi un nombre positif uwu")
                jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(
                    int(input("Choisis un nombre positif stp (surtout pas de nombre négatifs sinon je te goume")))
            if phrase == 3:
                print("Mais vas y je vais pas te manger sois pas timide plz passe moi un nombre positif")
                jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(
                    int(input("Choisis un nombre positif stp (surtout pas de nombre négatifs sinon je te goume")))
            if phrase == 4:
                print("Bon je vais pleurer dans mon coin si tu continue à me passer des nombres négatifs snif snof")
                jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(
                    int(input("Choisis un nombre positif stp (surtout pas de nombre négatifs sinon je te goume")))
            if phrase == 5:
                print("wola (ft Rémi)")
                jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(
                    int(input("Choisis un nombre positif stp (surtout pas de nombre négatifs sinon je te goume")))
        if nombre <= 0:
            print("OUIIIII merci tu khalass")
            break

jeu_pas_ouf_mais_rigolo_funne_meme_meme_funne(int(input("Choisis un nombre positif stp (surtout pas de nombre négatifs sinon je te goume: ")))