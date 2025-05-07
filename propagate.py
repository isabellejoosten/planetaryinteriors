import numpy as np
def Pressure(p, dpdivdr, delta_r):
    p += dpdivdr*delta_r
    return p

def Mass(M, r, delta_r, rho):
    func = 4*np.pi*rho*r**2
    M += func*delta_r
    return M

def Gravity(G, M, r):
    g = (G*M)/(r**2)
    return G

def Radius(r, delta_r):
    r += delta_r