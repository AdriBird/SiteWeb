def plus_proche(ville, dist, visitee):
    '''
    Permet de déterminer la ville la plus proche non visitée de la ville dans laquelle le voyageur si situe
    '''
    min_ville = dist[ville][0]
    for i in range(len(dist)-1):
        if ville != i:
            if dist[ville][i] < dist[ville][i+1] and dist[ville][i] < min_ville:
                min_ville = dist[ville][i]
    #print("On va de", villes[i-1], "à", villes[i], min_ville)
    return min_ville

def voyageur(villes, dist, depart):
    for i in range(len(villes)-1):

        print("On va de", villes[i], "à", villes[i+1], "en", plus_proche(i, dist, [True, True, False, False, False]))

villes = ["Nancy", "Metz", "Paris", "Reims", "Troyes"]
dist = [[0,55,303,188,183],[55,0,306,176,203],[303,306,0,142,153],[188,176,142,0,123],[183,203,153,123,0]]
visitee = [True, True, False, False, False]
voyageur(villes, dist, 0)