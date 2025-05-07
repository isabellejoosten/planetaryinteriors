import propagate
import numpy as np
import matplotlib.pyplot as plt

rtotal = 467000            #radius in [m]
delta_r = 10                #step size in [m]
Mtotal = 94.3*10**20       #mass of Europa in [kg]
rho = 2210
G = 6.67430*10**(-11)

r = np.arange(0, rtotal + delta_r, delta_r)
M = np.zeros(len(r))
p = np.zeros(len(r))
g = np.zeros(len(r))

for i in range(0, len(r)-1):
    M[i+1] = propagate.Mass(M[i], r[i+1], delta_r, rho)

for i in range(len(r)):
    g[i] = propagate.Gravity(G, M[i], r[i])

#gflip = np.flip(g)
for i in np.flip(range(1, len(r))):
    p[i-1] = propagate.Pressure(p[i], rho, g[i], delta_r)

#plt.plot(p,r)
#plt.show()
print(p[0], p[1], p[2])
print(M[0], M[1], M[2])
print(g[0], g[1], g[2])
print(r[0], r[1], r[2])