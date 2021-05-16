#m = [[5 for i in range(8)]for j in range(8)]
t = [m[i][j]for i in range(8) for j in range(8)]

for i in range(8):
    for j in range(8):
        t[8*i+j]=m[i][j]
print(t)









