



def conv_base2_to_base10(x):
    n = 1
    c = 0
    while x > 0:
        if x % 2 == 1 :
            c += n
            x -= 1
        n = 2*n
        x = x/10
    return c





