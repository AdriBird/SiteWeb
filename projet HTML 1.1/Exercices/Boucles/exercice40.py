from random import *

def choix_nombre(min, max):
    nombre = randint(min, max)
    print("L'ordinateur a trouvé son nombre")
    return nombre
alea = choix_nombre(int(input("Chiffre minimum: ")), int(input("Chiffre maximum: ")))


def jeu(hypothèse):
    trouve = 1
    while trouve == 1:
        if hypothèse > alea:
            print("plus petit!")
            hypothèse = int(input("Dommage! Retente ta chance: "))
        if hypothèse < alea:
            print("Plus grand!")
            hypothèse = int(input("Dommage! Retente ta chance: "))
        if hypothèse == alea:
            print("Bien joué, tu as trouvé le bon nombre!")
            trouve = 0

jeu(int(input("Choisis un nombre: ")))

















"GG bg t'as trouvé le nombre caché! Tu as gagné ma fierté !"