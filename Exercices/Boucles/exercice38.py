def conv_base10_to_base2(a):
    res = ""
    while a >= 1:
        b = int(a%2)
        a /= 2
        res += str(b)
        res = res[::-1]
    print(res, "(base2)")



def conv_base2_to_base10(a):
    res = 0
    pre = 0
    a = a[::-1]
    for i in range(len(a)):
        pre = int(a[i]) * (2 ** i)
        res += pre
    print(res, "(base10)")

"""
def conv_base2_to_base10(a):
    res = 0
    pre = 0
    for i in range(len(a)):
        pre = int(a[i]) * (2 ** (len(a) -i -1) )
        res += pre
    print(res)
"""

while True:
    #conv_base2_to_base10(str(input("Nombre (base2): ")))
    conv_base10_to_base2(int(input("Nombre (base10): ")))