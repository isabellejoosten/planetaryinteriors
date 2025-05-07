import propagate
import numpy as np

rtotal = 1565000            #radius of Europa in [m]
delta_r = 1                 #step size in [m]
Mtotal = 479.7*10**20       #mass of Europa in [kg]
rho = 3020

r = np.arange(0, rtotal + delta_r, delta_r)
M = np.zeros(len(r))
M[0] = 0                    # initial condition (mass at centre)

for i in range(0, len(r)-1):
    M[i+1] = propagate.Mass(M[i], r[i+1], delta_r, rho)

print(M[-1])