def couple_distant(tab, a, b):
    end=0
    for i in range(len(tab)):
        if tab[i] == a:
            end+=1
        if tab[i] == b and end == 1:
            end+=1
        if end == 2:
            print(True)
            return

    print(False)


couple_distant([0,6,2,3,1,5], 1, 0)