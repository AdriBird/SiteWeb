alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def ordre(m1, m2):
    lettre = 0
    while alphabet.index(m1[lettre]) == alphabet.index(m2[lettre]):
        lettre += 1
        if m1 == m2:
            print("bruh j'ai dit deux mots différents u muffin head")
            break
    if alphabet.index(m1[lettre]) < alphabet.index(m2[lettre]):
        print("Le mot", m1, "est placé avant", m2, "dans le dictionnaire.")
    if alphabet.index(m1[lettre]) > alphabet.index(m2[lettre]):
        print("Le mot", m1, "est placé après", m2, "dans le dictionnaire.")




ordre(str(input("Écris un mot: ")), str(input("Écris un deuxième mot: ")))