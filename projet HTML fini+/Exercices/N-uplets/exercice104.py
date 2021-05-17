


# 1
def extrema (t) :
    mi = t[0]
    ma = t[0]
    for element in t :
        if element < mi :
            mi = element
        elif element > ma :
            ma = element
    return mi, ma

# 2
print (extrema([8,5,6,4,3,9,4,0,12,6]))






