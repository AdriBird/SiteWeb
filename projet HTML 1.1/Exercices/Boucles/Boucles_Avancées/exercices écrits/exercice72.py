from time import *
from matplotlib.pyplot import *







debut = perf_counter()
a = 0
n = 10000
'''for i in range(1000):
    a = a + 1
print(a)

for i in range(n):
    a = a + 1
for j in range(n):
    a = a + 1
'''
for i in range(n):
    for j in range(n):
        a = a + 1
print(a)
fin = perf_counter()
print("Temps passé :", (fin - debut))