

def premiers_entiers1 (x):
    """première posibilitée"""
    d = {}
    for i in range (x):
        d[i]= i**3
    return d

def premiers_entiers2 (x):
    """deuxième posibilitée"""
    f = {i : i**3 for i in range (x)}
    return f


print (premiers_entiers1 (10))
print (premiers_entiers2 (10))