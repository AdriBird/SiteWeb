def annonce(num, prov, dest):
    if dest != "0":
        msg = "le train n°" + str(num) + " en provenance de " + prov + " et à destination de" + dest + "entre en gare"
    else:
        msg = "le train n°" + str(num) + "en provenance de " + prov + "entre en gare. Ce train est terminus Arnaque-la-poste."
    print(msg)

annonce("5768", "Bonneville", "0")
