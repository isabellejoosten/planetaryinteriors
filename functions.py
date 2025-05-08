import numpy as np

def inertia(r, rho, delta_r, M):
    inertia = 0
    for i in range(len(r)):
        inertia += delta_r*rho[i]*r[i]**4

    return inertia*(8*np.pi)/(3*M[-1]*r[-1]*r[-1])