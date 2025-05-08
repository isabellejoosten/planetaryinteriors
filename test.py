import numpy as np
import propagate
import functions

r = np.arange(0, 10 + 2, 2)
rho = np.zeros(len(r))
for j in range(3):
    for i in range(len(r)):
        if r[i] <= 5:
            rho[i] += 1
        else:
            rho[i] += 2
print(r)
print(rho) 