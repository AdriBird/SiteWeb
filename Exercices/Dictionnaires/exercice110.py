

def compare_tableaux (t,u):
    d_t = occurences (t)
    d_u = occurences (u)
    if len(d_u) != len(d_t):
        return False
    for i in d_t:
        if not i in d_u:
            return False
        elif d_t[i] != d_u[i]:
            return False
    return True