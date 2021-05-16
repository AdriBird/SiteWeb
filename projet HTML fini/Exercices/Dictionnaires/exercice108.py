

def occurences (t):
    d = {}
    for element in t:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
    return d
