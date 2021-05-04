def est_croissant (t):
    if len(t)==0:
        return None
    i=len(t)-1
    while i>0:
#        print("nouveau tour avec i =" , i)
        if t[i-1]<=t[i]:
            i-=1
        else:
            return False
    return True
assert est_croissant ([1,2,3,4])==True
assert est_croissant ([1,3,2,4])==False
assert est_croissant ([])==None