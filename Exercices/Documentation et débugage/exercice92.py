def est_croissante(t):
    i = len(t) - 1
    while i >= 0:
        if t[i] <= t[i+1]:
            print(True)
            return True
        else:
            print(False)
            return False
    i -= 1

#est_croissante([])
assert est_croissante([1,2,3,4]), "like ou meurs demain"
assert est_croissante([4,3,2,1])==False, "conséquences"