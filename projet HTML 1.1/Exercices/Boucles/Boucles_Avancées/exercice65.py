def doublon(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if j != i and t[i]==t[j]:
                print(True)
                return
    print(False)


doublon([0,1,2,3,4,5])