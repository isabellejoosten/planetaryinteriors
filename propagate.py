import numpy as np
def Pressure(p, rho, g, delta_r):
    func = -rho*g
    p = p - func*delta_r
    return p

def Mass(M, r, delta_r, rho):
    func = 4*np.pi*rho*r**2
    M += func*delta_r
    return M

def Gravity(G, M, r):
    if r == 0:
        g = 0
    else:
        g = G*M/r**2
    return g

def Radius(r, delta_r):
    r += delta_r