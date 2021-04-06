def sous_mot(tab1, tab2):
    for i in range(max(len(tab1), len(tab2))):
        if len(tab1) != len(tab2):
            print(False)
            return
        if tab1[i] != tab2[i]:
            print(False)
            return
    print(True)
sous_mot([0,1,2,3,4,5,6], [0,1,2,3,4,5,6])

