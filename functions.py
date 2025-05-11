import numpy as np

def inertia(r, rho, delta_r, M):
    inertia = 0
    for i in range(len(r)):
        inertia += delta_r*rho[i]*r[i]**4

    return inertia*(8*np.pi)/(3*M[-1]*r[-1]*r[-1])

def set_density(T, rho0, alphaT, K, p):
    rho = np.zeros(len(T))
    for i in range(len(T)):
        rho[i] = rho0*(1-alphaT*(T[0]-T[i])+(p[0]-p[i])/K)
    return rho

def get_rayleigh(rho, alpha, g, T, D, kappa, eta):
    Ra = np.zeros(len(T))
    for i in range(len(T)):
        Ra[i] = (rho[i]*alpha*g[i]*(T[0]-T[i])*D**3)/(kappa*eta)

    return Ra