



def conv_base10_to_base2(x):
    n = 1
    c = 0
    while x > 0:
        if x % 2 == 1 :
            c += n
            x -= 1
        n = 10*n
        x = x/2
    return c





