def element_commun(t1, t2):
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == t2[j]:
                print(True)
                return
    print(False)


element_commun([0,1,2,3,4], [5,6,7,8,9])