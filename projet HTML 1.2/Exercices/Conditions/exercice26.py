def annonce(num, prov, dest):
    if dest != "0":
        msg = "Le train n°" + str(num) + " en provenance de " + prov + " et à destination de " + dest + " entre en gare. "
    else:
        msg = "Le train n°" + str(num) + " en provenance de " + prov + " entre en gare. Ce train est terminus Arnaque-la-poste. "
    print(msg)

annonce(4557, "Paris", "Marseille")
annonce("5768", "Bonneville", "0")



# Première question : Le train n°4557 en provenance de Paris et à destination de Marseille entre en gare.
# Deuxième question : Le train n°5768 en provenance de Bonneville entre en gare. Ce train est terminus Arnaque-la-poste.

