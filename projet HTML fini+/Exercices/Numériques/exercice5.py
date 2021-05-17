

from time import time

st= time()
for i in range(50000):
	a=1.001**i
print(time()-st)

st= time()
for i in range(50000):
	a=2**i
print(time()-st)



