
def Eratosthène(n):
    t = [True]*n
    t[0]=False
    t[1]=False
    for i in range(n):
        if t[i] == True:
            for j in range(i+1, n):
                if j%i == 0:
                    t[j]=False
    return t


t=Eratosthène(10)
for i in range(10):
    if t[i]:
        print(i, end = ",")

